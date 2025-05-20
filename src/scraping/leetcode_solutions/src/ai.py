import os
import pandas as pd
from pathlib import Path
from openai import OpenAI
import pdb


def send_requests(files_path):
    data = pd.read_csv(files_path)

    # Read the data
    content = data['code'][125] + '\n\nLabel: ' + data['label'][125]

    # Send a request
    print(f"SENDING A REQUEST:\n {content}")

    # Generate
    generate(content, INSTRUCTIONS, CLIENT)


def generate(content, instructions, client):
    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": instructions},
            {
                "role": "user",
                "content": content,
            },
        ],
        stream=True,
    )
    
    # Response
    print("\nRESPONSE:\n")
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    API_KEY = os.environ["DEEPSEEK_API_KEY"]
    CLIENT = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

    INSTRUCTIONS = """
    You are a Python algorithms expert, specializing in mapping Python code to time complexity Big O labels.
    I will provide you with Python codes that are labeled with WORST-CASE big O time complexities. Your task is to evaluate the provided code sample and the mapped time complexity label, and output whether the label is correct or not. Answer with no only if the difference between the specified time complexity label and the real label is big, for example, if the time complexity might be O(1), and in some cases O(n), and the provided label is in one of the possible labels, answer with yes. 

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

            Label: nlogn

    Example response:
    yes
    """

    BASE_PATH = Path(__file__).parent

    print(BASE_PATH)
    files_path = BASE_PATH / "../data/parsed_files/original/clean_data.csv"

    send_requests(files_path)