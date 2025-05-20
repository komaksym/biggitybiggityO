import os
from pathlib import Path
import pandas as pd
from openai import OpenAI
import pdb


def send_requests(files_path):
    data_to_review = {'code': [], 'label': []}

    data = pd.read_csv(files_path)
    num_rows = data.shape[0]
    num_rows = 500

    # Read the data
    for i in range(num_rows):
        # Index the data row
        code = data.iloc[i]['code']
        label = data.iloc[i]['label']

        # Collect
        content = code + "\n\nLabel: " + label

        # Send a request
        print(f"SENDING A REQUEST ({i+1}/{num_rows}):\n {content}")

        # Generate
        print("\nRESPONSE:")
        response = generate(content, INSTRUCTIONS, CLIENT)
        print(response, end='\n\n')

        # Add data under question to a separate dataset for further review
        if response == 'no':
            data_to_review['code'].append(code)
            data_to_review['label'].append(label)

    # Save
    df = pd.DataFrame(data_to_review)

    # Path
    BASE_PATH = Path(__file__).parent
    save_path = BASE_PATH / "../data/parsed_files/ai_preprocessed/data_to_review.csv"

    df.to_csv(save_path, index=False)


def generate(content, instructions, client):
    request = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": content},
        ],
        stream=False
    )

    # Response
    response = request.choices[0].message.content
    return response
    


if __name__ == "__main__":
    API_KEY = os.environ["DEEPSEEK_API_KEY"]
    CLIENT = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

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

            Label: nlogn

    Example response:
    yes
    """

    BASE_PATH = Path(__file__).parent
    files_path = BASE_PATH / "../data/parsed_files/original/clean_data.csv"

    send_requests(files_path)
