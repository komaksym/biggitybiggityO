from pathlib import Path

import pandas as pd
from pandas import DataFrame


def get_file_dtype(path: Path | str) -> str:
    """Extract the .xyz extension of a file"""
    return str(path).split(".")[-1]


def read_data(source_path: Path) -> DataFrame:
    source_dtype: str = get_file_dtype(source_path)

    match source_dtype:
        case "json":
            data = pd.read_json(source_path)

        case "jsonl":
            data = pd.read_json(source_path, lines=True)

        case "csv":
            data: DataFrame = pd.read_csv(source_path)

        case _:
            raise ValueError("The source file must be in .csv / .json or .jsonl format.")

    return data


def save_data(data: DataFrame, target_path: Path | str) -> None:
    target_dtype: str = get_file_dtype(target_path)

    match target_dtype:
        case "json":
            data.to_json(target_path, index=False, orient="records")

        case "jsonl":
            data.to_json(target_path, lines=True, index=False, orient="records")

        case "csv":
            data.to_csv(target_path, index=False)
        
        case _:
            raise ValueError("The save file must be in .csv / .json or .jsonl format.")
