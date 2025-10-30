import re
from pathlib import Path

import pandas as pd

from .utils import read_data, save_data

BASE_LOCATION: Path = Path(__file__).parent


def format_labels(series: pd.Series) -> pd.Series:
    """Main format labels function."""

    def normalize_complexity(label: str) -> str:
        """Normalize labels"""

        label = label.replace(" ", "").lower()

        mapping: dict[str, str] = {
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

    def drop_labeled_x(data: pd.Series, value: str) -> pd.Series:
        """Drop samples where the value equals the argument"""

        return data[data != value]

    # Normalize labels
    normalized = series.apply(normalize_complexity)

    # Drop samples with "other" label
    return drop_labeled_x(normalized, value="other")


def format_codes(data: pd.Series) -> pd.Series:
    """Main format codes function."""

    def remove_comments(code_sample: str) -> str:
        """Remove in-code comments."""

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

    def process_code(code_sample: str) -> str:
        """Wrapper code processor."""

        if pd.isna(code_sample):
            return code_sample

        formatted_sample: str = remove_comments(str(code_sample))
        formatted_sample = strip_empty_lines(formatted_sample)

        return formatted_sample

    return data.apply(process_code)


def format_data(data: pd.DataFrame) -> pd.DataFrame:
    """Format data in the specified columns. (Main wrapper)"""

    required_columns: set[str] = {"code", "complexity"}
    missing_columns: list[str] = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    data["code"] = format_codes(data["code"])
    data["complexity"] = format_labels(data["complexity"])

    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)

    return data


if __name__ == "__main__":
    # Specify paths
    source_path: Path = BASE_LOCATION.parent / "data/leetcode-parsed/clean_leetcode_data.csv"
    out_path: Path = BASE_LOCATION.parent / "data/leetcode-parsed/clean_leetcode_data.csv"

    # Read data
    data: pd.DataFrame = read_data(source_path)

    # Format data
    formatted_data: pd.DataFrame = format_data(data)

    # Write changes
    save_data(formatted_data, out_path)
