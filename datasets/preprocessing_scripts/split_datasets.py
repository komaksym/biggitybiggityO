import pandas as pd
from sklearn.model_selection import train_test_split


class SplitDatasets:
    def __init__(self, input_path, output_path_train, output_path_test):
        self.input_path = input_path
        self.output_path_train = output_path_train
        self.output_path_test = output_path_test

        data = self.load_data(self.input_path)
        train_set, test_set = self.split_data(data)
        self.save_data(output_path_train, output_path_test, train_set, test_set)

    def load_data(self, dataset_path):
        dataset = pd.read_csv(dataset_path, sep=";", on_bad_lines="warn")
        return dataset

    def split_data(self, data):
        train_set, test_set = train_test_split(data, test_size=0.2, random_state=1)
        return train_set, test_set

    def save_data(self, save_path_train, save_path_test, train_set, test_set):
        train_set.to_csv(save_path_train, index=False)
        test_set.to_csv(save_path_test, index=False)


sample = SplitDatasets(
    "../processed_merged_dataset.csv", "../train_set.csv", "../test_set.csv"
)
