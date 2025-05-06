import re
from pathlib import Path


files_path = 'solutions/'
parsed_data = {'label': [], 'code': []}
corrupted_data = []


# Defie a cleaning pattern
def set_regex_pattern(pattern, flags=None):
    return re.compile(rf"{pattern}", flags)


# Read raw data
def search_files(folder_path):
    raw_data = {'file_paths': [], 'files': []}

    for file_path in (Path('.').glob(f'{files_path}/*.py')):
         raw_data['files'].append(file_path.read_text())
         raw_data['file_paths'].append(file_path)

    return raw_data


# Clean raw data and write
def clean_files(files, save_paths, filter_pttrn):
    for file, save_path in zip(files, save_paths):
        match = re.sub(filter_pttrn, '', file)
        save_path.write_text(match)


# Regex pattern
filter_pttrn = set_regex_pattern(r"#\s*?Space.*?\n", flags=re.DOTALL)

# Read raw data
raw_data = search_files(files_path)

# Clean the data up
clean_files(raw_data['files'], raw_data['file_paths'], filter_pttrn)