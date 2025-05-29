import re
from pathlib import Path

from utils import open_corrupted_files, search_files, set_regex_pattern

BASE_LOCATION = Path(__file__).parent


class FileParser:
    def __init__(self):
        pass

    def parse_labels(self, text, regex_pattern=r"\sO\("):
        """
        Parsing labels (Time complexity) until the number
        of closing parentheses matches the number of open parantheses.
        """
        results = []

        regex_pattern = regex_pattern
        matches = re.finditer(regex_pattern, text)

        for match in matches:
            # Start position to begin searching from
            start_pos = match.end()
            # Index for searching parentheses
            i = start_pos
            # Number of opened parentheses
            depth = 1

            while i < len(text) and depth > 0:
                if text[i] == "(":
                    depth += 1
                elif text[i] == ")":
                    depth -= 1

                # Keep searching
                i += 1

            # Add to results if depth was exhausted
            if depth == 0:
                results.append(text[start_pos : i - 1])

        return results

    def separate_annotated_labels(
        self, files_path, files, regex_pattern=r"#.*?O\(.*\n(?:#.*O.*\n)+"
    ):
        """
        Separate files with annotated labels e.g. where there's
        a separate time complexity label for every operation in a single solution.
        """
        annotations_pattern = set_regex_pattern(regex_pattern)
        annotated_data = []

        # Check every file
        for path, file in zip(files_path, files):
            label_matches = re.findall(annotations_pattern, file)

            # Save paths
            for _ in label_matches:
                annotated_data.append(path)

        # Move data to a separate folder
        open_corrupted_files(
            "mv", annotated_data, destination_path="solutions/annotated_solutions/"
        )
        print(f"Moved: {len(annotated_data)} files")

    def parse_files(self, file_paths, files, code_pattern):
        """
        Parse data and gather separatelly based on
        whether the number of labels in a file matches the number of solutions.
        """
        parsed_data = {"code": [], "label": []}
        corrupted_data = []

        # Regex pattern to remove in-code comments
        filter_pattern = set_regex_pattern(
            r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})",
            flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
        )

        for path, file in zip(file_paths, files):
            code_matches = re.findall(code_pattern, file)
            label_matches = self.parse_labels(file)

            # Number of samples doesn't equal num of labels
            if len(code_matches) != len(label_matches):
                corrupted_data.append(path)
                continue

            for code, label in zip(code_matches, label_matches):
                # Remove in-code comments
                code = re.sub(filter_pattern, "", code)

                parsed_data["label"].append(label)
                parsed_data["code"].append(code)

        return parsed_data, corrupted_data


if __name__ == "__main__":
    src_files_path = BASE_LOCATION.parent / "data/raw_files/messy_files/unclear_files"

    # Get the data into Python objects
    raw_data = search_files(src_files_path)

    # Regex patterns
    code_pattern = set_regex_pattern(
        r"(?:#\sTime.*?\n)(.*?)(?=#\sTime|\Z)", flags=re.DOTALL | re.MULTILINE
    )
    # code_pattern = set_regex_pattern(r"(?:class|def)\sSolution")

    # Start parsing
    parser = FileParser()
    parsed_data, corrupted_data = parser.parse_files(
        **raw_data, code_pattern=code_pattern
    )

    print(f"Successfully parsed: {len(parsed_data['label'])} files")
    print(f"Unsuccessfully parsed: {len(corrupted_data)} files")

    # Open for review on demand
    open_corrupted_files("open", corrupted_data)

    """# Move on demand
    open_corrupted_files("mv", corrupted_data, "solutions/unclear_solutions/")
    print(f"Number of moved files: {len(corrupted_data)}")"""
