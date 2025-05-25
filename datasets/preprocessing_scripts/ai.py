import os
from pathlib import Path
import pandas as pd
from openai import AsyncOpenAI
import asyncio
from asyncio import Semaphore


class LLM:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.counter = 1

    async def send_requests(self, sem, instructions, request, num_requests, **kwargs):
        async with sem:
            response = await self.client.chat.completions.create(
                model=self.model,
                **kwargs,
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": request},
                ],
                stream=False,
            )
            # Response
            response = response.choices[0].message.content

            # Log 
            print(f"\nREQUEST (#{self.counter}/{num_requests}): {request}")
            print("\nRESPONSE:\n", response, end='\n\n')

            self.counter += 1

            return response


class Audit:
    def __init__(self, source_path, llm, sem):
        self.data_to_review = {"code": [], "complexity": []}
        self.data = pd.read_csv(source_path, sep=";")

        self.llm = llm
        self.sem = sem

    async def process_requests(self, instructions):
        # Collect requests
        requests = [
            code + "\n\nComplexity: " + complexity
            for code, complexity in zip(self.data["code"], self.data["complexity"])
        ]

        # Total # of data samples
        num_requests = len(requests)

        # Create tasks in the form of coroutine objects
        tasks = [
            self.llm.send_requests(
                self.sem, instructions, request, num_requests,
            )
            for request in requests
        ]

        # Run coroutines concurrently
        responses = await asyncio.gather(*tasks)

        # Process responses
        self.process_responses(responses)

    def process_responses(self, responses):
        for i, response in enumerate(responses):
            # Add data under question to a separate dataset for further review
            if response == "no":
                self.data_to_review["code"].append(self.data['code'].iloc[i])
                self.data_to_review["complexity"].append(self.data['complexity'].iloc[i])

        print(f"Number of labels under question: {len(self.data_to_review)}")


    def save_data_to_review(self, save_path):
        # Save
        df = pd.DataFrame(self.data_to_review)
        df.to_csv(save_path, index=False)


async def main():
    # Client
    client = AsyncOpenAI(
        api_key=os.environ["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
    )
    model = 'grok-3'

    INSTRUCTIONS = """
    You are a Python algorithms expert, specializing in mapping Python code to time complexity Big O labels.
    I will provide you with Python codes that are labeled with WORST-CASE big O time complexities. Your task is to evaluate the provided code sample and the mapped time complexity label, and output whether the label is correct or not. Answer with no only if the difference between the specified time complexity label and the real label is big, for example, if the time complexity might be O(1), and in some cases O(n), and the provided label is in one of the possible labels, answer with yes, or if the specified time complexity label is correct but doesn't include a constant, omit it and answer yes as the difference is insignificant compared to if the specified label was n, but the actual label was logn or nlogn or n^2.

    You should respond only with yes or no.

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

            Complexity: O(nlogn)

    Example response:
    yes
    """

    BASE_PATH = Path(__file__).parent
    source_path = BASE_PATH / "../data/clean_leetcode_data.csv"
    save_path = BASE_PATH / "../data/ai_audited/clean_leetcode_data.csv"

    # LLMs to use
    grok = LLM(client, model)
    semaphore = Semaphore(5)

    # Initiate audit
    audit = Audit(source_path, grok, semaphore)
    # Send requests
    await audit.process_requests(INSTRUCTIONS)
    # Save data for review
    audit.save_data_to_review(save_path)


if __name__ == "__main__":
    asyncio.run(main())