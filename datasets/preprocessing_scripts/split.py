import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
from pandas import DataFrame

BASE_PATH: Path = Path(__file__).parent


class SplitDatasets:
    def __init__(self, source_path: Path, output_path_train: Path, output_path_test: Path) -> None:
        # Paths
        self.source_path: Path = source_path
        self.output_path_train: Path = output_path_train
        self.output_path_test: Path = output_path_test

        # Load data
        data: DataFrame = self.load_data(self.source_path)

        # Split data
        train_dataset, test_dataset = self.split_data(data)

        # GUESS WHAT? ... Save data
        self.save_data(output_path_train, output_path_test, train_dataset, test_dataset)

    def load_data(self, dataset_path: Path) -> DataFrame:
        dataset: DataFrame = pd.read_csv(dataset_path, sep=";", on_bad_lines="warn")
        return dataset

    def split_data(self, data: DataFrame) -> tuple[DataFrame, DataFrame]:
        train_set: DataFrame
        test_set: DataFrame

        train_set, test_set = train_test_split(data, test_size=0.2, random_state=1)
        return train_set, test_set

    def save_data(
        self, save_path_train: Path, save_path_test: Path, train_set: DataFrame, test_set: DataFrame
    ) -> None:
        train_set.to_csv(save_path_train, index=False)
        test_set.to_csv(save_path_test, index=False)


if __name__ == "__main__":
    # Paths
    source_path: Path = BASE_PATH / "../processed_merged_dataset.csv"
    output_path_train: Path = BASE_PATH / "../train_set.csv"
    output_path_test: Path = BASE_PATH / "../test_set.csv"

    # Split
    sample = SplitDatasets(source_path, output_path_train, output_path_test)
