import asyncio
import os
import types
from asyncio import Semaphore
from pathlib import Path
from typing import Any

from sklearn.metrics import f1_score

import pandas as pd
from openai import AsyncOpenAI
from openai.types.chat.chat_completion import ChatCompletion

BASE_PATH: Path = Path(__file__).parent


class LLM:
    def __init__(self, client: AsyncOpenAI, model: str) -> None:
        self.client: AsyncOpenAI = client
        self.model: str = model

    async def send_requests(
        self, sem: Semaphore, instructions: str, request: str, num_requests: int, request_id: int = 0, **kwargs
    ) -> str | None:
        """
        Send async requests to a LLM,
        where the num of concurrent requests is capped by a semaphore.
        """
        try:
            async with sem:
                response: ChatCompletion = await self.client.chat.completions.create(
                    model=self.model,
                    **kwargs,
                    messages=[
                        {"role": "system", "content": instructions},
                        {"role": "user", "content": request},
                    ],
                    stream=False,
                )
                # Parse response
                response_content: str | None = response.choices[0].message.content

                # Log
                print(f"\nREQUEST: (#{request_id}/{num_requests}):\n{request}")
                print("\nRESPONSE:\n", response_content, end="\n\n")


                return response_content

        except Exception as e:
            print(f"Request #{request_id} failed. {e}")
            return None


class Evaluate:
    def __init__(self, source_path: Path, llm: LLM, sem: Semaphore) -> None:
        self.llm: LLM = llm
        self.sem: Semaphore = sem

        # Prep the output data
        self.llm_preds: dict[str, list[str | None]] = {}

        # Load the data
        self.data: pd.DataFrame = pd.read_csv(source_path)
        self.labels = self.data["complexity"].str.replace(" ", "")

        # Handle potential absence of the column, or an empty dataframe
        if "code" not in self.data.columns:
            raise ValueError("Dataset must contain a 'code' column")
        if self.data.empty:
            raise ValueError("Dataset is empty")

    async def process_requests(self, instructions: str) -> list[str | None]:
        """
        Collect all requests at once, send them all at once,
        gather responses, and then send respones for processing.
        """
        # Collect requests
        requests: list[str] = [code for code in self.data["code"]]

        # Total # of requests
        num_requests: int = len(requests)

        # Create tasks in the form of coroutine objects
        tasks: list[types.CoroutineType[Any, Any, str | None]] = [
            self.llm.send_requests(
                self.sem,
                instructions,
                request,
                num_requests,
                request_id = i+1
            )
            for i, request in enumerate(requests)
        ]

        # Run coroutines concurrently
        return await asyncio.gather(*tasks)
        
    def process_responses(self, responses: list[str | None]) -> None:
        """
        Just pour all responses into a df.
        """
        llm_predictions = []

        for response in responses:
            # Add LLM's decision
            llm_predictions.append(response)

        return llm_predictions

    def evaluate(self, preds):
        label2id, id2label = dict(), dict()

        for id, label in enumerate(set(self.labels)):
            id2label[id] = label
            label2id[label] = id

        def map_func(x):
            return label2id.get(x, -1)

        # Encode 
        self.labels = self.labels.apply(map_func)
        preds = [map_func(pred) for pred in preds]

        # Result
        f1_score_ = f1_score(self.labels, preds, average="macro")
        return f1_score_
    
    def save_results(self, model_name, result, output_path):
        new_data = pd.DataFrame({'model_name': [model_name], 'f1-macro': [result]})

        # If some data already exists
        if output_path.exists():
            # Read the already existing data
            main = pd.read_csv(output_path)
            # Concatenate the new one to the existing data
            combined = pd.concat([main, new_data], ignore_index=True)
            # Save the combined version
            combined.to_csv(output_path, index=False)
        else:
            # Save data for verification
            new_data.to_csv(output_path, index=False)

        


async def main() -> None:
    # Client
    client = AsyncOpenAI(
        api_key=os.environ["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
    )
    model = "grok-3"

    # Test client
    #client = AsyncOpenAI(
        #api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com"
    #)
    #model = "deepseek-chat"
    
    #client = AsyncOpenAI(
        #api_key=os.environ["OPENAI_API_KEY"],
        #base_url="https://api.openai.com/v1",
    #)
    #model = "gpt-5"

    eval_instruction = """
    You are a Python algorithms expert, specializing in mapping Python code to time complexity Big O labels.  
    I will provide you with Python codes. Your task is to evaluate the provided code sample, and output evaluated, correct WORST-CASE time complexity label.  
    You should drop constants when evaluating a time complexity label, for example: instead of O(2n^2) you should drop 2 and just output O(n^2).

    You should choose from O(1), O(logn), O(n), O(nlogn), O(n ^ 2), O(n ^ 3), np as your output label.

    Your response shouldn't contain anything but a label. One word. 

    Example input:
        "class Solution(object):
            def minimumLines(self, stockPrices):
                def gcd(a, b):
                    while b:
                        a, b = b, a%b
                    return a
            
                stockPrices.sort()
                result = 0
                prev = None
                for i in range(1, len(stockPrices)):
                    dy, dx = stockPrices[i][1]-stockPrices[i-1][1], stockPrices[i][0]-stockPrices[i-1][0]
                    g = gcd(dy, dx)
                    if not prev or prev != (dy//g, dx//g):
                        prev = (dy//g, dx//g)
                        result += 1
                return result"	

    Example response:  
        O(nlogn)
    """

    source_path: Path = BASE_PATH.parents[1] / "test_set.csv"
    save_path: Path = BASE_PATH / "results.csv"

    # LLM to use
    llm = LLM(client, model)
    semaphore = Semaphore(10)

    # Initiate audit
    eval = Evaluate(source_path, llm, semaphore)
    # Send requests
    responses = await eval.process_requests(eval_instruction)
    # Process responses
    preds = eval.process_responses(responses)
    # Evaluate
    result = eval.evaluate(preds)
    # Add result
    eval.save_results(model_name=model, result=result, output_path=save_path)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyError as e:
        print(f"Missing environmental variable: {e}")
        exit(1)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)
