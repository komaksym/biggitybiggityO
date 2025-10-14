import asyncio
import os
import types
from asyncio import Semaphore
from pathlib import Path
from typing import Any

from config import SYS_PROMPT_EXPONENTIAL, SYS_PROMPT_FACTORIAL

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
                # Response
                response_content: str | None = response.choices[0].message.content

                # Log
                print(f"\nREQUEST: (#{request_id}/{num_requests}):\n{request}")
                print("\nRESPONSE:\n", response, end="\n\n")


                return response_content

        except Exception as e:
            print(f"Request #{request_id} failed. {e}")
            return None


class Generate:
    def __init__(self, source_path: Path, llm: LLM, sem: Semaphore) -> None:
        self.llm: LLM = llm
        self.sem: Semaphore = sem

        # Prep the output data
        self.feature_name: str = f"{self.llm.model}_decision"
        self.llm_decisions: dict[str, list[str | None]] = {self.feature_name: []}

        # Load the data
        self.data: pd.DataFrame = read_data(source_path)

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
        for response in responses:
            # Add LLM's decision
            self.llm_decisions[f"{self.llm.model}_decision"].append(response)

    def save_data_to_review(self, save_path: Path) -> None:
        """
        Join responses with the original data and save.
        """
        # Create a directory in case one doesn't exist yet
        save_path.parent.mkdir(parents=True, exist_ok=True)

        # Join the original df with LLM decisions
        joined: pd.DataFrame = self.data.join(pd.DataFrame(self.llm_decisions))
        # Save
        save_data(joined, save_path)


async def main() -> None:
    # Client
    client = AsyncOpenAI(
        api_key=os.environ["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
    )
    model = "grok-3"

    # Test client
    """client = AsyncOpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com"
    )
    model = "deepseek-chat"
    """

    eval_instruction = """
    You are a Python algorithms expert, specializing in mapping Python code to time complexity Big O labels.  
    I will provide you with Python codes. Your task is to evaluate the provided code sample, and output evaluated, correct WORST-CASE time complexity label.  
    You should drop constants when evaluating a time complexity label, for example: instead of O(2n^2) you should drop 2 and just output O(n^2).

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

    source_path: Path = BASE_PATH.parent / "data/leetcode-parsed/messy_leetcode_data.csv"
    save_path: Path = BASE_PATH.parent / "data/leetcode-parsed/ai_audited/relabeled_messy_leetcode_data.csv"

    # LLM to use
    grok = LLM(client, model)
    semaphore = Semaphore(10)

    # Initiate audit
    audit = Audit(source_path, grok, semaphore)
    # Send requests
    responses = await audit.process_requests(eval_instruction)
    # Process responses
    audit.process_responses(responses)
    # Save data for review
    audit.save_data_to_review(save_path)


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
