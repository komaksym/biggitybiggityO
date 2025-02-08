import json


class LabelFormatter:
    def __init__(self):
        # Reading JSON file
        with open("../scraped_python_data.jsonl", "r") as file:
            self.data = [json.loads(line) for line in file]

        # Start formatting
        self.format()
        # Write changes
        self.save_formatted_json()

    def format_time_complexity(self, complexity):
        match complexity:
            case "O(1)":
                return "constant"

            case "O(\\log n)":
                return "logn"

            case "O(n)":
                return "linear"

            case "O(n \\log n)":
                return "nlogn"

            case "O(n ^ 2)":
                return "quadratic"

            case "O(n ^ 3)":
                return "cubic"

            case "O(2 ^ n)":
                return "np"

            case _:
                return "other"

    def format(self):
        for sample in self.data:
            sample["time_complexity"] = self.format_time_complexity(
                sample["time_complexity"]
            )

    def save_formatted_json(self):
        with open("../scraped_python_data.jsonl", "w") as file:
            for line in self.data:
                file.write(json.dumps(line) + "\n")


# Call
foo = LabelFormatter()
foo.format()
