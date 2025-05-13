import re
from pathlib import Path
import subprocess
import pdb
import pandas as pd


def set_regex_pattern(pattern, flags=0):
    return re.compile(rf"{pattern}", flags)


def search_files(folder_path):
    raw_data = {'file_paths': [], 'files': []}

    for file_path in (Path('.').glob(f'{files_path}/*.py')):
         raw_data['file_paths'].append(file_path)
         raw_data['files'].append(file_path.read_text())

    return raw_data


def parse_labels(text):
    """Parsing labels (Time complexity)"""
    results = []

    pattern = r'\sO\('
    matches = re.finditer(pattern, text) 
    for match in matches:
        # Start position to begin searching from
        start_pos = match.end()
        # Index for searching parentheses
        i = start_pos 
        # Number of opened parentheses
        depth = 1

        while i < len(text) and depth > 0:
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1

            # Keep searching
            i += 1

        # Add to results if depth was exhausted
        if depth == 0:
            results.append(text[start_pos:i-1])
           
    return results


def separate_annotated_labels(files_path, files):
    annotations_pattern = set_regex_pattern(r"#.*?O\(.*\n(?:#.*O.*\n)+")
    annotated_data = []

    for path, file in zip(files_path, files): 
        label_matches = re.findall(annotations_pattern, file)

        for label in label_matches:
            annotated_data.append(path)

    # Move data to a separate folder
    open_corrupted_files("mv", annotated_data, destination_path='solutions/annotated_solutions/')
    print(f"Moved: {len(annotated_data)} files")


def parse_data(files_path, files):
    for path, file in zip(files_path, files): 
        code_matches = re.findall(CODES_PATTERN, file)
        label_matches = parse_labels(file)

        if len(code_matches) != len(label_matches):
            corrupted_data.append(path)
            continue

        for i, (code, label) in enumerate(zip(code_matches, label_matches)):
            # Remove comments
            code = re.sub(FILTER_PATTERN, "", code) 

            parsed_data['label'].append(label)
            parsed_data['code'].append(code)


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
    subprocess.run(paths)


#CODES_PATTERN = set_regex_pattern(r"(?:class|def)\sSolution")
CODES_PATTERN = set_regex_pattern(r"(?:#\sTime.*?\n)(.*?)(?=#\sTime|\Z)", flags=re.DOTALL | re.MULTILINE)
FILTER_PATTERN = set_regex_pattern(r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})", flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)

files_path = 'solutions/'
parsed_data = {'code': [], 'label': []}
corrupted_data = []

raw_data = search_files(files_path)
parse_data(raw_data['file_paths'], raw_data['files'])
print("The data was successfully parsed.")

df = pd.DataFrame(parsed_data)
df.to_csv("clean_data.csv", index=False)
print("The data was successfully saved.")

#print(f"Unsuccessfully parsed file paths: {corrupted_data}")
#print(f"Successfully parsed: {len(parsed_data['label'])} files")
#print(f"Unsuccessfully parsed: {len(corrupted_data)} files")

#for idx, code in enumerate(parsed_data['code'][50:100]):
    #print(f"CODE #{idx+1}:\n", code, end='\n\n')

#open_corrupted_files("open", corrupted_data)
#open_corrupted_files("mv", corrupted_data, "solutions/unclear_solutions/")
#print(f"Number of moved files: {len(corrupted_data)}")