from pathlib import Path

import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from typing import Any

BASE_LOCATION: Path = Path(__file__).parent


class DatasetSplitter:
    def __init__(self, source_path: Path, output_path_train: Path, output_path_test: Path) -> None:
        self.source_path = source_path
        self.output_path_train = output_path_train
        self.output_path_test = output_path_test

    def load_data(self) -> DataFrame:
        """Load dataset from CSV file."""

        if not self.source_path.exists():
            raise FileNotFoundError(f"Source file not found: {self.source_path}")

        data: DataFrame = pd.read_csv(self.source_path, sep=",", on_bad_lines="warn")

        if data.empty:
            raise ValueError("Dataset is empty")

        return data

    def split_data(
        self, data: DataFrame, test_size: float = 0.2, random_state: int = 42
    ) -> list[Any]: 
        """Split data into train and test sets."""

        if not 0 < test_size < 1:
            raise ValueError(f"Test size must be between 0 and 1, got: {test_size}")

        return train_test_split(data, test_size=test_size, random_state=random_state)

    def save_data(self, train_set: DataFrame, test_set: DataFrame) -> None:
        """Save the data to CSV files."""

        # Create output directories if needed
        self.output_path_train.parent.mkdir(parents=True, exist_ok=True)
        self.output_path_test.parent.mkdir(parents=True, exist_ok=True)

        train_set.to_csv(self.output_path_train, index=False)
        test_set.to_csv(self.output_path_test, index=False)

    def run(self, test_size: float = 0.2, random_state: int = 42) -> None:
        """Execute the whole split workflow."""

        data: DataFrame = self.load_data()
        train_set, test_set = self.split_data(data, test_size, random_state)
        self.save_data(train_set, test_set)


if __name__ == "__main__":
    try:
        # Define paths
        source_path: Path = BASE_LOCATION.parent / "processed_merged_dataset.csv"
        output_path_train: Path = BASE_LOCATION.parent / "train_set.csv"
        output_path_test: Path = BASE_LOCATION.parent / "test_set.csv"

        # Split dataset
        splitter = DatasetSplitter(source_path, output_path_train, output_path_test)
        splitter.run()

    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"Error: {e}")
        exit(1)

