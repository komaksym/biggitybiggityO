import re
from pathlib import Path
import pdb


files_path = 'solutions/'
parsed_data = {'label': [], 'code': []}
corrupted_data = []


def set_regex_pattern(pattern, flags=None):
    return re.compile(rf"{pattern}", flags)


def search_files(folder_path):
    raw_data = {'file_paths': [], 'files': []}

    for file_path in (Path('.').glob(f'{files_path}/*.py')):
         raw_data['file_paths'].append(file_path)
         raw_data['files'].append(file_path.read_text())

    return raw_data


def parse_data(files_path, files):
    for path, file in zip(files_path, files): 
        code_matches = re.findall(CODES_PATTERN, file)
        label_matches = re.findall(LABELS_PATTERN, file)

        if len(code_matches) != len(label_matches):
            corrupted_data.append(path)
            continue

        for i, (code, label) in enumerate(zip(code_matches, label_matches)):
        
            code = re.sub(FILTER_PATTERN, "", code[0]) 

            parsed_data['label'].append(label)
            parsed_data['code'].append(code)



CODES_PATTERN = set_regex_pattern(r"(?:
LABELS_PATTERN = set_regex_pattern(r"
FILTER_PATTERN = set_regex_pattern(r"


raw_data = search_files(files_path)
parse_data(raw_data['file_paths'], raw_data['files'])

print(f"Successfully parsed: {len(parsed_data['label'])} files")
print(f"Unsuccessfully parsed: {len(corrupted_data)} files")
print(f"Unsuccessfully parsed file paths: {corrupted_data}")














    
