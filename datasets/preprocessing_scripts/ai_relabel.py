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
            print(f"\nREQUEST: (#{self.counter}/{num_requests}):\n{request}")
            print("\nRESPONSE:\n", response, end='\n\n')

            self.counter += 1

            return response


class Audit:
    def __init__(self, source_path, llm, sem):
        self.llm_decisions = {'grok_decision2': []}
        self.data = pd.read_csv(source_path, sep=",")

        self.llm = llm
        self.sem = sem

    async def process_requests(self, instructions):
        # Collect requests
        requests = [code for code in self.data["code"]]

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
        for response in responses:
            # Add LLM's decision
            self.llm_decisions['grok_decision2'].append(response)

    def save_data_to_review(self, save_path):
        # Join the original df with LLM decisions
        joined = self.data.join(pd.DataFrame(self.llm_decisions))

        # Save
        joined.to_csv(save_path, index=False)


async def main():
    # Client
    client = AsyncOpenAI(
        api_key=os.environ["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
    )
    model = 'grok-3'

    # Test
    #client = AsyncOpenAI(
    #    api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com"
    #)
    #model = "deepseek-chat"

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

    BASE_PATH = Path(__file__).parent
    source_path = BASE_PATH / "../data/ai_audited/audited_clean_leetcode_data.csv"
    save_path = BASE_PATH / "../data/relabeled_audited_clean_leetcode_data.csv"
    save_path = source_path

    # LLMs to use
    grok = LLM(client, model)
    semaphore = Semaphore(5)

    # Initiate audit
    audit = Audit(source_path, grok, semaphore)
    # Send requests
    await audit.process_requests(eval_instruction)
    # Save data for review
    audit.save_data_to_review(save_path)


if __name__ == "__main__":
    asyncio.run(main())