import re
from pathlib import Path
import subprocess
import pandas as pd


# Defie a cleaning pattern
def set_regex_pattern(pattern, flags=0):
    return re.compile(rf"{pattern}", flags)


# Read raw data
def search_files(folder_path):
    raw_data = {'file_paths': [], 'files': []}

    for file_path in (Path('.').glob(f'{folder_path}**/*.py')):
         raw_data['files'].append(file_path.read_text())
         raw_data['file_paths'].append(file_path)

    return raw_data


# Clean raw data and write
def clean_files(files, file_paths, filter_pttrn):
    parsed_data = {'code': [], 'label': []}
    corrupted_data = []
    num_of_duplicates = 0

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
            if label and len(parsed_data['label']) - len(parsed_data['code']) < 1:
                parsed_data['label'].append('\n'.join(label))
            
            # Check if it's the definition of solution
            if i < len(lines) and re.search(r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE):

                # Keep consuming until a label from the next solution is hit
                while i < len(lines) and not re.search(r"#.*\sO\(", lines[i]):
                    code.append(lines[i])
                    next_label_exists = True
                    i += 1

                    # If no next label was found (from the next solution)
                    if i < len(lines) and re.search(r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE):
                        num_of_duplicates += 1
                        next_label_exists = False
                        # New solution was found, break out of the loop
                        break

                # Add the code snippet
                solution = re.sub(filter_pttrn, "", '\n'.join(code))
                parsed_data['code'].append(solution)

                # If there was no label at the beginning, add a placeholder
                if len(parsed_data['code']) > len(parsed_data['label']):
                    parsed_data['label'].append('')
                
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
        if len(parsed_data['label']) != len(parsed_data['code']):
            corrupted_data.append(file_path)
            
    print(f"Number of duplicates: {num_of_duplicates}.")

    return parsed_data, corrupted_data


def open_corrupted_files(command, posix_paths, destination_path=None):
    # Subprocess command
    command = command
    paths = [command]

    # Populate the paths
    for p in posix_paths:
    # Get the str representation of PosixPath
        paths.append(str(p))

    # If moving files
    if command == 'mv' and destination_path:
        paths.append(destination_path)

    # Run
    if posix_paths:
        subprocess.run(paths)


if __name__ == '__main__':
    # Path to files
    files_path = 'raw_files/messy_files/'

    print("Searching files...")
    # Read raw data
    raw_data = search_files(files_path)
    print(f"Successfully found {len(raw_data['files'])} files.")

    # Regex pattern
    FILTER_PATTERN = set_regex_pattern("(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})", flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)

    print("Cleaning the files...")
    # Clean the data up
    parsed_data, corrupted_data = clean_files(raw_data['files'], raw_data['file_paths'], FILTER_PATTERN)

    print("Successfully finished cleaning the data.")
    print(f"Unsuccessfully cleaned {len(corrupted_data)} files.")

    # Inspect corrupted files
    open_corrupted_files('open', corrupted_data)

    df = pd.DataFrame(parsed_data)
    df.to_csv("messy_data.csv", index=False)

    print(f"Successfully saved {len(parsed_data['code'])} solutions.")