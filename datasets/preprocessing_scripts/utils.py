from pathlib import Path

import pandas as pd


def get_file_extension(path: Path) -> str:
    """Extract the file extension without a dot."""
    return Path(path).suffix.lstrip(".")


def read_data(source_path: Path) -> pd.DataFrame:
    """Read data from CSV, JSON, or JSONL file."""
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    extension: str = get_file_extension(source_path)

    match extension:
        case "json":
            return pd.read_json(source_path)

        case "jsonl":
            return pd.read_json(source_path, lines=True)

        case "csv":
            return pd.read_csv(source_path)

        case _:
            raise ValueError(f"Unsupported file format. .{extension}. Use .csv, .json, .jsonl instead.")


def save_data(data: pd.DataFrame, target_path: Path) -> None:
    """Save data to CSV, JSON, or JSONL file."""
    target_path.mkdir(parents=True, exist_ok=True)

    extension: str = get_file_extension(target_path)

    match extension:
        case "json":
            data.to_json(target_path, index=False, orient="records")

        case "jsonl":
            data.to_json(target_path, lines=True, index=False, orient="records")

        case "csv":
            data.to_csv(target_path, index=False)

        case _:
            raise ValueError(f"Unsupported file format. .{extension}. Use .csv, .json, .jsonl instead.")
