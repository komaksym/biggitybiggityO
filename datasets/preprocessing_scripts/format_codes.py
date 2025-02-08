import pandas as pd
import re


class CodeFormatter:
    def __init__(self) -> None:
        self.data = pd.read_csv("../processed_dataset.csv", sep=";")

        # Applying filtering
        self.data["code"] = self.run_filtering(self.data["code"])

        # Saving the results
        self.data.to_csv("../processed_dataset.csv", index=False)

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


cf = CodeFormatter()
