import json
import pandas as pd
from pathlib import Path


class LabelFormatter:
    def __init__(self, source_path, save_path=None, label_col_name="complexity"):
        self.save_path = source_path if save_path is None else save_path

        self.source_dtype = str(source_path).split('.')[-1]
        self.save_dtype = str(save_path).split('.')[-1]

        # Read data
        self.read_data(source_path)

        # Start formatting
        self.format(label_col_name)

        # Write changes
        self.save_formatted_json()

    def read_data(self, source_path):
        # Data in .json or .jsonl
        if self.source_dtype == 'json' or self.source_dtype == 'jsonl':
            with open(source_path, "r") as file:
                self.data = [json.loads(line) for line in file]

        # If data in .csv
        elif self.source_dtype == 'csv':
            self.data = pd.read_csv(source_path, sep=',')

    def format_time_complexity(self, complexity):
        match complexity:
            case "1" | "O(1)" | "# Time:  O(1)":
                return "other"

            case "logn" | "O(logn)" | "# Time:  O(logn)":
                return "other"

            case "n" | "O(n)" | "# Time:  O(n)":
                return "other"

            case "nlogn" | "O(nlogn)" | "# Time:  O(nlogn)":
                return "other"

            case "n^2" | "O(n ^ 2)" | "O(n^2)" | "# Time:  O(n^2)" | "# Time:  O(n ^ 2)":
                return "other"

            case "n^3" | "O(n ^ 3)" | "# Time:  O(n^3)" | "# Time:  O(n ^ 3)":
                return "other"

            case "n!" | "O(n!)" | "# Time:  O(n!)":
                return "other"

            case "2^n" | "O(2 ^ n)" | "# Time:  O(2^n)" | "# Time:  O(2 ^ n)":
                return "other"

            case "np" | "O(np)" | "# Time:  O(np)":
                return "other"

            #case _:
                #return "other"

    def format(self, label_col_name):
        if self.source_dtype == 'json' or self.source_dtype == 'jsonl':
            for sample in self.data:
                sample[label_col_name] = self.format_time_complexity(
                    sample[label_col_name]
                )
        
        elif self.source_dtype == 'csv':
            self.data[label_col_name] = self.data[label_col_name].apply(self.format_time_complexity)

    def save_formatted_json(self):
        match self.save_dtype:
            # Save in .jsonl
            case 'jsonl':
                with open(self.save_path, "w") as file:
                    for line in self.data:
                        file.write(json.dumps(line) + "\n")

            # Save in .json
            case 'json':
                with open(self.save_path, "w") as file:
                    file.write(json.dumps(self.data))
                
            # Save in .csv
            case 'csv':
                """Before storing as .csv need to convert to a pd.DataFrame"""

                # Source is in .jsonl, meaning reading by lines
                if self.source_dtype == 'jsonl':
                    self.data = pd.read_json(self.data, lines=True)

                # Source is in .json, reading as a whole
                elif self.source_dtype == 'json':
                    self.data = pd.read_json(self.data, lines=True)

                # Saving to .csv
                self.data.to_csv(self.save_path, index=False)


if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent

    source_path = BASE_PATH / "../data/leetcode-parsed/messy_leetcode_data.csv"
    save_path = BASE_PATH / "../data/leetcode-parsed/unclear_labels_messy_leetcode_data.csv"

    # Call
    foo = LabelFormatter(source_path, save_path, "label")
    
