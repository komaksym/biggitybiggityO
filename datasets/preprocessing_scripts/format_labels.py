import json
from pathlib import Path


class LabelFormatter:
    def __init__(self, source_path, save_path=None):
        self.save_path = source_path if save_path is None else save_path

        # Reading JSON file
        with open(source_path, "r") as file:
            self.data = [json.loads(line) for line in file]

        # Start formatting
        self.format()
        # Write changes
        self.save_formatted_json()

    def format_time_complexity(self, complexity):
        match complexity:
            case "O(1)":
                return "O(1)"

            case "O(\\log n)":
                return "O(logn)"

            case "O(n)":
                return "O(n)"

            case "O(n \\log n)":
                return "O(nlogn)"

            case "O(n ^ 2)":
                return "O(n ^ 2)"

            case "O(n ^ 3)":
                return "O(n ^ 3)"

            case "O(2 ^ n)":
                return "O(2 ^ n)"
            
            case "O(n!)":
                return "O(n!)"

            case _:
                return "other"

    def format(self):
        for sample in self.data:
            sample["time_complexity"] = self.format_time_complexity(
                sample["time_complexity"]
            )

    def save_formatted_json(self):
        with open(self.save_path, "w") as file:
            for line in self.data:
                file.write(json.dumps(line) + "\n")


if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent

    source_path = BASE_PATH / "../data/neetcode_data.jsonl"
    save_path = BASE_PATH / "../data/neetcode_data.jsonl"

    # Call
    foo = LabelFormatter(source_path, save_path)
    foo.format()
