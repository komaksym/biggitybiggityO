import re
from pathlib import Path
import subprocess
import pdb


files_path = 'solutions/'
parsed_data = {'label': [], 'code': []}
corrupted_data = []


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
    annotated_data = []

    for path, file in zip(files_path, files): 
        label_matches = re.findall(ANNOTATIONS_PATTERN, file)

        for label in label_matches:
            annotated_data.append(path)

    # Move data to a separate folder
    open_corrupted_files("mv", annotated_data, destination_path='solutions/annotated_solutions/')
    print(f"Moved: {len(annotated_data)} files")


def parse_data(files_path, files):
    for path, file in zip(files_path, files): 
        code_matches = re.findall(CODES_PATTERN, file)
        label_annotations = re.findall(ANNOTATIONS_PATTERN, file)
        label_matches = parse_labels(file)

        if len(code_matches) != len(label_matches):
            corrupted_data.append(path)
            continue

        for i, (code, label) in enumerate(zip(code_matches, label_matches)):
            # Remove comments
            code = re.sub(FILTER_PATTERN, "", code) 

            parsed_data['label'].append(label)
            parsed_data['code'].append(code)


def open_corrupted_files(command, posix_paths, destination_path):
    # Subprocess command
    command = command
    paths = [command]

    # Populate the paths
    for p in posix_paths:
    # Get the str representation of PosixPath
        paths.append(str(p))

    paths.append(destination_path)
    # Run
    subprocess.run(paths)


CODES_PATTERN = set_regex_pattern(r"^(?:class|def).*?((?:\n#\s*?Time)|(?:\Z))", flags=re.DOTALL | re.MULTILINE)
FILTER_PATTERN = set_regex_pattern(r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})", flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)
ANNOTATIONS_PATTERN = set_regex_pattern(r"#.*?O\(.*\n(?:#.*O.*\n)+")


raw_data = search_files(files_path)
separate_annotated_labels(raw_data['file_paths'], raw_data['files'])
#parse_data(raw_data['file_paths'], raw_data['files'])

#print(f"Successfully parsed: {len(parsed_data['label'])} files")
#print(f"Unsuccessfully parsed: {len(corrupted_data)} files")
#print(f"Unsuccessfully parsed file paths: {corrupted_data}")

#open_corrupted_files("open", corrupted_data)







    
"""
Regex pattern for parsing time complexity labels, 
only what's inside of the brackets, e.g. 'O(n^2)' results in 'n^2'.

We do that by using a non-capturing group and positive lookahead assertion,
which are techniques that are very useful when you want to match your target substring
by using some parts of a string as a guide but you do not want it to be parsed as a result
and so you exclude it, a.k.a. 'not capture' or 'lookahead' (you just look, dont extract)
"""

"""
Regex pattern for parsing codes

We're matching the codes that start with 'class' continued by
a non-greedy amount of arbitrary symbols, newlines included (hence flag DOTALL)
until we meet a return clause, which is suffixed with a non-greedy amount of symbols
in the same row
"""




