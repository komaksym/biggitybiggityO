import re
from pathlib import Path

import pandas as pd

from utils import open_corrupted_files, search_files, set_regex_pattern

BASE_LOCATION = Path(__file__).parent


class FileCleaner:
    def __init__(self):
        self.parsed_data = {"code": [], "label": []}
        self.corrupted_data = []
        self.num_of_duplicates = 0

    def clean(self, files, file_paths, regex_pattern):
        """Iterate files line by line and duplicate labels for solutions 
           that do not have its own label by taking the predecessor.

           The idea is for every solution to have its own label which will get
           the files into a common format that we can then parse.

           We also save 'corrupted' data, where there was not even a single label
           to borrow for solutions.
           """
        for file, file_path in zip(files, file_paths):
            lines = file.splitlines()

            label = []
            code = []
            i = 0
            next_label_exists = True

            while i < len(lines):
                # Keep capturing while complexity comments are present
                while i < len(lines) and re.search(r"#.*\sO\(", lines[i]):
                    label.append(lines[i])
                    i += 1

                # Add the label only once before a solution is added
                if (
                    label
                    and len(self.parsed_data["label"]) - len(self.parsed_data["code"])
                    < 1
                ):
                    self.parsed_data["label"].append("\n".join(label))

                # Check if it's the definition of solution
                if i < len(lines) and re.search(
                    r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE
                ):
                    # Keep consuming until a label from the next solution is hit
                    while i < len(lines) and not re.search(r"#.*\sO\(", lines[i]):
                        code.append(lines[i])
                        next_label_exists = True
                        i += 1

                        # If no next label was found (from the next solution)
                        if i < len(lines) and re.search(
                            r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE
                        ):
                            self.num_of_duplicates += 1
                            next_label_exists = False
                            # New solution was found, break out of the loop
                            break

                    # Add the code snippet
                    solution = re.sub(regex_pattern, "", "\n".join(code))
                    self.parsed_data["code"].append(solution)

                    # If there was no label at the beginning, add a placeholder
                    if len(self.parsed_data["code"]) > len(self.parsed_data["label"]):
                        self.parsed_data["label"].append("")

                    # Reset the current label only if the next one exists, else keep it for further borrowing
                    if next_label_exists:
                        label = []

                    # Reset the current label and code snippet
                    code = []

                    # Rewind one step back to account for the main iteration
                    i -= 1

                # Next line
                i += 1

            # Make sure we have the same number of solutions as labels
            if len(self.parsed_data["label"]) != len(self.parsed_data["code"]):
                self.corrupted_data.append(file_path)

        print(f"Number of duplicates: {self.num_of_duplicates}.")

        return self.parsed_data, self.corrupted_data

    def save(self, data_to_save, path):
        if not str(path).endswith(".csv"):
            raise ValueError("Make sure the type of the file to save is '.csv'")

        df = pd.DataFrame(data_to_save)
        df.to_csv(path, index=False)

        print(f"Successfully saved {len(data_to_save['code'])} solutions.")


if __name__ == "__main__":
    # Absolute path to script's directory
    fp_source = BASE_LOCATION.parent / "data/raw_files/messy_files/annotated_files"

    # Read raw data
    raw_data = search_files(fp_source)

    # Regex pattern
    filter_pattern = set_regex_pattern(
        "(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})",
        flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )

    # Clean the data up
    cleaner = FileCleaner()
    parsed_data, corrupted_data = cleaner.clean(
        **raw_data, regex_pattern=filter_pattern
    )

    # Inspect corrupted files
    open_corrupted_files("open", corrupted_data)

    # Save parsed data
    save_path = BASE_LOCATION.parent / "test.csv"
    cleaner.save(parsed_data, save_path)