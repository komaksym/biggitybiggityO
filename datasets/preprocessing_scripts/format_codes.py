import pandas as pd
import re
from pathlib import Path


class CodeFormatter:
    def __init__(self, source_path, save_path) -> None:
        self.data = pd.read_json(source_path, lines=True)

        # Applying filtering
        self.data["src"] = self.run_filtering(self.data["src"])

        # Saving the results
        self.data.to_json(save_path, orient="records", lines=True)


    def remove_comments(self, code_sample):
        return re.sub(
            r"(#.+?$)|([\"']{3,}.+?[\"']{3,})",
            "",
            code_sample,
            flags=re.MULTILINE | re.DOTALL,
        )

    def strip_empty_lines(self, code_sample):
        filtered_code = []

        for line in code_sample.split("\n"):
            line = line.rstrip()

            if line == "":
                if filtered_code and filtered_code[-1] != "":
                    filtered_code.append(line)
                else:
                    continue
            else:
                filtered_code.append(line)
        return "\n".join(filtered_code)

    def run_filtering(self, data):
        for i in range(len(data)):
            data[i] = self.remove_comments(data[i])
            data[i] = self.strip_empty_lines(data[i])

        return data


if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent

    source_path = BASE_PATH / "../data/codecomplex_data.jsonl"
    save_path = BASE_PATH / "../data/codecomplex_data.jsonl"

    cf = CodeFormatter(source_path, save_path)