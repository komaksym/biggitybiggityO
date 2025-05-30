import re
from pathlib import Path
from typing import Any

import pandas as pd
from pandas import DataFrame

from .utils import read_data, save_data

BASE_PATH: Path = Path(__file__).parent


class LabelFormatter:
    def __init__(self, source_path: Path, out_path: Path) -> None:
        # Read data
        data: DataFrame = read_data(source_path)

        # Start formatting
        data["complexity"] = self.format(data["complexity"])

        # Write changes
        save_data(data, out_path)

    def rename_labels(self, complexity: str) -> str:
        match complexity:
            case "1" | "O(1)":
                return "O(1)"

            case "logn" | "O(logn)":
                return "O(logn)"

            case "n" | "O(n)":
                return "O(n)"

            case "nlogn" | "O(nlogn)":
                return "O(nlogn)"

            case "n^2" | "O(n ^ 2)" | "O(n^2)":
                return "O(n ^ 2)"

            case "n^3" | "O(n ^ 3)":
                return "O(n ^ 3)"

            case "n!" | "O(n!)":
                return "O(n!)"

            case "2^n" | "O(2 ^ n)":
                return "O(2 ^ n)"

            case "np" | "O(np)":
                return "O(np)"

            case _:
                return "other"

    def format(self, data: pd.Series) -> Any:
        return data.apply(self.rename_labels)


class CodeFormatter:
    def __init__(self, source_path: Path, out_path: Path) -> None:
        data: DataFrame = read_data(source_path)

        # Start formatting
        data["code"] = self.format(data["code"])

        # Write changes
        save_data(data, out_path)

    def remove_comments(self, code_sample: str) -> str:
        return re.sub(
            r"(#.+?$)|([\"']{3,}.+?[\"']{3,})",
            "",
            code_sample,
            flags=re.MULTILINE | re.DOTALL,
        )

    def strip_empty_lines(self, code_sample: str) -> str:
        """
        Remove consecutive empty lines and keep only 1 between code lines.
        """
        filtered_code: list[str] = []

        for line in code_sample.split("\n"):
            line: str = line.rstrip()

            if line == "":
                # If previous line is not another empty line
                if filtered_code and filtered_code[-1] != "":
                    filtered_code.append(line)
                else:
                    continue
            else:
                filtered_code.append(line)

        return "\n".join(filtered_code)

    def format(self, data: pd.Series) -> pd.Series:
        return data.apply(self.remove_comments).apply(self.strip_empty_lines)


if __name__ == "__main__":
    source_path: Path = BASE_PATH / "../data/leetcode-parsed/clean_leetcode_data.csv"
    out_path: Path = BASE_PATH / "../data/leetcode-parsed/clean_leetcode_data.csv"

    LabelFormatter(source_path, out_path)
    CodeFormatter(source_path, out_path)
