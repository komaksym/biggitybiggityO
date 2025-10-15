import asyncio
import os
import types
from asyncio import Semaphore
from pathlib import Path
from typing import Any

from config import EVAL_SYS_PROMPT, USER_EVALUATE_PROMPT

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
    def __init__(self, LLMs: list[LLM], sem: Semaphore, source_path: Path) -> None:
        self.LLMs = LLMs
        self.sem: Semaphore = sem

        # Model names
        self.models = [f"{LLM.model}" for LLM in self.LLMs]

        # Human data with examples to built prompts
        try:
            self.data_to_eval = pd.read_csv(source_path)
        except ValueError:
            print("The data could not be loaded.")

        # Create feature names based on llm names
        self.feature_names: list[str] = [f"{model}_decision" for model in self.models]
        # Add new column to DF. LLM's decision (if doesn't exist yet)
        if self.feature_names not in self.data_to_eval.columns.to_list(): # (not sure if this syntax works)
            self.data_to_eval[self.feature_names] = ""

        # Handle potential absence of the column, or an empty dataframe
        if "code" not in self.data_to_eval.columns or "complexity" not in self.data_to_eval.columns:
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

        # Prep responses
        responses = {f"{feature}": [] for feature in self.feature_names}

        # Total # of requests
        num_requests: int = len(requests)

        # Create tasks in the form of coroutine objects
        tasks: list[types.CoroutineType[Any, Any, str | None]] = [
            [LLM.send_requests(self.sem, system_instructions, request, num_requests, request_id=i + 1)
            for i, request in enumerate(requests)] for LLM in self.LLMs
        ]

        # Run coroutines concurrently for all models
        for task, model in zip(tasks, self.models):
            responses[model] = await asyncio.gather(*task)
        
        return responses

    def process_responses(self, responses) -> None:
        """
        Just pour all responses into a df.
        """
        responses = pd.DataFrame(responses)
        breakpoint()
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
    # Clients
    deepseek_client = AsyncOpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
    deepseek_model = "deepseek-chat"

    grok_client = AsyncOpenAI(api_key=os.environ["XAI_API_KEY"], base_url="https://api.x.ai/v1")
    grok_model = "grok-4-fast-reasoning"

    gemini_client = AsyncOpenAI(
        api_key=os.environ["GEMINI_API_KEY"],
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    gemini_model = "gemini-2.5-flash"

    # Path for examples which we are randomly going to provide to the model
    source_path: Path = BASE_PATH.parent / "data/data_for_evaluation/data_for_eval.csv"
    # Output path
    output_path: Path = BASE_PATH.parent / "data/synthetic_data/synthetic_data.csv"

    # LLMs to use for evaluation
    deepseek_llm = LLM(deepseek_client, deepseek_model)
    grok_llm = LLM(grok_client, grok_model)
    gemini_llm = LLM(gemini_client, gemini_model)

    # Gather LLMs
    LLMs = [deepseek_llm, grok_llm, gemini_llm]

    # Number of concurrent requests
    semaphore = Semaphore(10)

    # Initiate audits
    evaluate = Evaluate(LLMs, semaphore, source_path=source_path)

    # Send requests
    responses = await evaluate.process_requests(USER_EVALUATE_PROMPT, EVAL_SYS_PROMPT)
    # Process responses
    evaluate.process_responses(responses)
    


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyError as e:
        print(f"Missing environmental variable: {e}")
        exit(1)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        exit(1)