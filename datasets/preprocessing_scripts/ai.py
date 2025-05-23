import os
from pathlib import Path
import pandas as pd
from openai import OpenAI
import pdb


class LLM:
    def __init__(self, client, model):
        self.client = client
        self.model = model

    def generate(self, instructions, content, *args, **kwargs):
        request = self.client.chat.completions.create(
            model=self.model,
            *args,
            **kwargs,
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": content},
            ],
            stream=False,
        )

        # Response
        response = request.choices[0].message.content
        return response


class Audit:
    def __init__(self, source_path, llm1, llm2):
        self.data_to_review = {"code": [], "complexity": [], 'model': []}
        self.data = pd.read_csv(source_path, sep=";")

        self.gemini = llm1
        self.grok = llm2

    def send_requests(self, instructions):
        num_rows = self.data.shape[0]
        num_rows = 100

        # Read the data
        for i in range(num_rows):
            # Index the data row
            code = self.data.iloc[i]["code"]
            complexity = self.data.iloc[i]["complexity"]

            # Collect
            content = code + "\n\nComplexity: " + complexity

            # Send a request
            print(f"SENDING A REQUEST ({i + 1}/{num_rows}):\n {content}")

            gemini_response = self.gemini.generate(instructions, content, reasoning_effort='medium')
            grok_response = self.grok.generate(instructions, content)

            # Generate
            print("\nRESPONSE from Gemini:\n", gemini_response, end='\n\n')
            print("\nRESPONSE from Grok:\n", grok_response, end='\n\n')

            # Add data under question to a separate dataset for further review
            if gemini_response == "no":
                self.data_to_review["code"].append(code)
                self.data_to_review["complexity"].append(complexity)
                self.data_to_review['model'].append('gemini')

            elif grok_response == "no":
                self.data_to_review["code"].append(code)
                self.data_to_review["complexity"].append(complexity)
                self.data_to_review['model'].append('grok')


    def save_data_to_review(self, save_path):
        # Save
        df = pd.DataFrame(self.data_to_review)
        df.to_csv(save_path, index=False)


if __name__ == "__main__":
    # Keys
    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
    XAI_API_KEY = os.environ["XAI_API_KEY"]
    
    # Clients
    GEMINI_CLIENT = OpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    XAI_CLIENT = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )

    # LLMs
    llms = {
        'gemini': {'client': GEMINI_CLIENT, 'model': 'gemini-2.5-pro-preview-05-06'}, 
        'xai': {'client': XAI_CLIENT, 'model': 'grok-3'},
        }

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
    gemini = LLM(**llms['gemini'])
    grok = LLM(**llms['xai'])

    # Initiate audit
    audit = Audit(source_path, gemini, grok)
    # Send requests
    audit.send_requests(INSTRUCTIONS)
    # Save data for review
    audit.save_data_to_review(save_path)