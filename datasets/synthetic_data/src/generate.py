import asyncio
import os
import types
from asyncio import Semaphore
from pathlib import Path
from typing import Any

from config import SYS_PROMPT_EXPONENTIAL, SYS_PROMPT_FACTORIAL, NUM_OF_EXAMPLES, NUM_OF_REQUESTS

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


class Generate:
    def __init__(self, llm: LLM, sem: Semaphore, num_of_samples: int, examples_path: Path) -> None:
        self.llm: LLM = llm
        self.sem: Semaphore = sem

        # Num of samples to generate
        self.num_of_requests = num_of_samples

        # Human data with examples to built prompts 
        try:
            self.examples = pd.read_csv(examples_path)
        except ValueError:
            print("The data was not loaded.")

        # Prep the output data
        self.feature_name: str = f"{self.llm.model}_decision"
        self.llm_decisions: dict[str, list[str | None]] = {self.feature_name: []}

        # Handle potential absence of the column, or an empty dataframe
        if "code" not in self.examples.columns:
            raise ValueError("Dataset must contain a 'code' column")
        if self.examples.empty:
            raise ValueError("Dataset is empty")

    def pick_random_example(self, num_of_examples):
        # Sample k number of data points
        k_samples = self.examples.sample(n=num_of_examples, random_state=42)
        return k_samples.code, k_samples.complexity

    def build_requests(self, base_user_instruction):
        # Starting prompt for each prompt
        starting_prompt = f"{base_user_instruction}\nEXAMPLES:\n\n"

        # Prompts that we are building
        prompts = [starting_prompt] * self.num_of_requests

        # Build specified number of requests
        for i in range(self.num_of_requests):
        # Read the real data
            # Pick random K number of real data examples
            codes, complexities = self.pick_random_example(NUM_OF_EXAMPLES)

            # Add Input => Output schema that maps label => code snippet to our prompts
            for code, complexity in zip(codes, complexities):
                # Add multiple examples to a single prompt
                prompts[i] += f"Input:\n{complexity}\nOutput:\n{code}\n"
        
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
        pass


async def main() -> None:
    # Main Client
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url="https://api.openai.com/v1")
    model = "gpt-5"

    # Cheap testing client
    client = AsyncOpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
    model = "deepseek-chat"

    # Path for examples which we are randomly going to provide to the model
    examples_path: Path = BASE_PATH.parent / "data/real_data/exponential_data.csv"

    # System prompt
    sys_prompt = SYS_PROMPT_EXPONENTIAL
    label = "O(2 ^ n)"
    user_prompt = f"""
    Generate as many python code snippets as you can that have big O time complexity of {label}.
    Code snippets should be separated with <SEP> token with newline before it and after it.
    """

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
