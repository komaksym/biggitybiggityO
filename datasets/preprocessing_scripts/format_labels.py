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
            case "constant":
                return "O(1)"

            case "logn":
                return "O(logn)"

            case "linear":
                return "O(n)"

            case "nlogn":
                return "O(nlogn)"

            case "quadratic":
                return "O(n ^ 2)"

            case "cubic":
                return "O(n ^ 3)"

            case "np":
                return "np"

            case _:
                return "other"

    def format(self):
        for sample in self.data:
            sample["complexity"] = self.format_time_complexity(
                sample["complexity"]
            )

    def save_formatted_json(self):
        with open(self.save_path, "w") as file:
            for line in self.data:
                file.write(json.dumps(line) + "\n")


if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent

    source_path = BASE_PATH / "../data/codecomplex_data.jsonl"
    save_path = BASE_PATH / "../data/codecomplex_data.jsonl"

    # Call
    foo = LabelFormatter(source_path, save_path)
    foo.format()
