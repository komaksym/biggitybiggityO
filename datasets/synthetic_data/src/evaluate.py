import asyncio
import os
import types
from asyncio import Semaphore
from pathlib import Path
from typing import Any

from config import EVAL_SYS_PROMPT

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
                print("\nRESPONSE:\n", response_content, end="\n\n")

                return response_content

        except Exception as e:
            print(f"Request #{request_id} failed. {e}")
            return None


class Evaluate:
    def __init__(self, llm: LLM, sem: Semaphore, source_path: Path) -> None:
        self.llm: LLM = llm
        self.sem: Semaphore = sem

        # Human data with examples to built prompts 
        try:
            self.data_to_eval = pd.read_csv(source_path)
        except ValueError:
            print("The data could not be loaded.")

        self.feature_name: str = f"{self.llm.model}_decision"
        # Add new column to DF. LLM's decision (if doesn't exist yet)
        if self.feature_name not in self.data_to_eval:
            self.data_to_eval[self.feature_name] = ""
        
        # Handle potential absence of the column, or an empty dataframe
        if "code" not in self.data_to_eval.columns or "label" not in self.data_to_eval.columns:
            raise ValueError("Dataset must contain a 'code' column")
        if self.data_to_eval.empty:
            raise ValueError("Dataset is empty")

    def build_requests(self, base_user_instruction):
        # Starting prompt for each prompt
        starting_prompt = f"{base_user_instruction}"

        # Num of samples to evaluate
        num_of_rows = self.data_to_eval.shape[0]

        # Prompts that we are building
        prompts = [starting_prompt] * num_of_rows

        for i in range(num_of_rows):
            # Extract code and label from dataframe
            code = self.data_to_eval.iloc[i].code
            label = self.data_to_eval.iloc[i].complexity

            # Build a prompt
            prompts[i] += f"Code: {code}\n\nLabel: {label}"
        
        return prompts

    async def process_requests(self, user_instructions, system_instructions: str) -> list[str | None]:
        """
        Collect all requests at once, send them all at once,
        gather responses, and then send respones for processing.
        """
        # Collect requests
        requests = self.build_requests(user_instructions)

        # Total # of requests
        num_requests: int = len(requests)

        # Create tasks in the form of coroutine objects
        tasks: list[types.CoroutineType[Any, Any, str | None]] = [
            self.llm.send_requests(self.sem, system_instructions, request, num_requests, request_id=i + 1)
            for i, request in enumerate(requests)
        ]

        # Run coroutines concurrently
        return await asyncio.gather(*tasks)

    def process_responses(self, responses: list[str | None]) -> None:
        """
        Just pour all responses into a df.
        """
        self.data_to_eval[self.feature_name] = responses
        return self.data_to_eval

def approve_samples(source_path, output_path):
    # Read the data
    data_to_approve = pd.read_csv(source_path)

    # Prep synthetic data
    synthetic_data = pd.DataFrame({"code": [], "complexity": []})

    # Extract decision columns
    decision_cols = [col for col in data_to_approve.columns if col.endswith("decision")]

    def vote(row, column_voters):
        num_of_yeses_to_approve = 2
        pass


async def main() -> None:
    # Client
    deepseek_client = AsyncOpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
    deepseek_model = "deepseek-chat"

    grok_client = AsyncOpenAI(api_key=os.environ["XAI_API_KEY"], base_url="https://api.x.ai/v1")
    grok_model = "grok-code-fast-1"

    gemini_client = AsyncOpenAI(api_key=os.environ["GEMINI_API_KEY"], base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
    gemini_model = "gemini-2.5-flash"

    # Path for examples which we are randomly going to provide to the model
    examples_path: Path = BASE_PATH.parent / "data/real_data/exponential_data.csv"

    # System prompt
    sys_prompt = SYS_PROMPT_EXPONENTIAL
    label = "O(2 ^ n)"
    user_prompt = f"Generate a python code snippet that has big O time complexity of {label}"

    # LLM to use
    llm = LLM(client, model)
    semaphore = Semaphore(10)

    # Initiate audit
    generate = Generate(llm, semaphore, num_of_samples=NUM_OF_REQUESTS, examples_path=examples_path)
    # Send requests
    responses = await generate.process_requests(user_prompt, sys_prompt)
    # Process responses
    #audit.process_responses(responses)


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
