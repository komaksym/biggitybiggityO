import re
from pathlib import Path

from pandas import DataFrame, Series

from .utils import read_data, save_data

BASE_PATH: Path = Path(__file__).parent


def format_labels(series: Series) -> Series:
    def normalize_complexity(label: str) -> str:
        """Normalize labels"""
        label = label.replace(" ", "").lower()

        mapping = {
            "1": "O(1)",
            "o(1)": "O(1)",
            "logn": "O(logn)",
            "o(logn)": "O(logn)",
            "n": "O(n)",
            "o(n)": "O(n)",
            "nlogn": "O(nlogn)",
            "o(nlogn)": "O(nlogn)",
            "n^2": "O(n^2)",
            "o(n^2)": "O(n^2)",
            "o(n^3)": "O(n^3)",
            "n^3": "O(n^3)",
            "n!": "O(n!)",
            "o(n!)": "O(n!)",
            "2^n": "O(2^n)",
            "o(2^n)": "O(2^n)",
            "np": "O(np)",
            "o(np)": "O(np)",
        }

        return mapping.get(label, "other")

    def drop_labeled_x(data: Series, value: str) -> Series:
        """Drop samples where the value equals the argument"""
        index = data.apply(lambda row: row == value).index
        data.drop(index, inplace=True)

        return data

    # Normalize labels
    series = series.apply(normalize_complexity)

    # Drop samples with "other" label
    return drop_labeled_x(series, value="other")


def format_codes(data: Series) -> Series:
    def remove_comments(code_sample: str) -> str:
        return re.sub(
            r"(#.+?$)|([\"']{3,}.+?[\"']{3,})",
            "",
            code_sample,
            flags=re.MULTILINE | re.DOTALL,
        )

    def strip_empty_lines(code_sample: str) -> str:
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

    return data.apply(remove_comments).apply(strip_empty_lines)


def format_data(data: DataFrame) -> DataFrame:
    data["code"] = data["code"].apply(format_codes)
    data["complexity"] = data["complexity"].apply(format_labels)

    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)

    return data


if __name__ == "__main__":
    # Paths
    source_path: Path = BASE_PATH / "../data/leetcode-parsed/clean_leetcode_data.csv"
    out_path: Path = BASE_PATH / "../data/leetcode-parsed/clean_leetcode_data.csv"

    # Data
    data: DataFrame = read_data(source_path)

    # Format
    formatted_data = format_data(data)

    # Write changes
    save_data(data, out_path)
