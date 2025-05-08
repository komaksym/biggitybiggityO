import re
from pathlib import Path


files_path = 'solutions/'
parsed_data = {'label': [], 'code': []}
corrupted_data = []


# Defie a cleaning pattern
def set_regex_pattern(pattern, flags=0):
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


def main():
    # Read raw data
    raw_data = search_files(files_path)

    # Regex patterns
    ## Remove space complexity comments
    space_comp_pttrn = set_regex_pattern(r"^#\s*Space.*?\n", flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
    ## Remove inline comments
    inline_commnts_ptrn = set_regex_pattern(r"[^\n]#.*")
    ## Remove docstrings 
    docstrings_pttrn = set_regex_pattern(r"(\"{3}.*?\"{3}\s*)|('{3}.*?'{3}\s*)", flags=re.DOTALL | re.IGNORECASE)
    ## Code comments
    line_commnts_ptrn = set_regex_pattern(r"^[^\n#]\s*#.*\n", flags=re.MULTILINE)


    # Clean the data up
    clean_files(raw_data['files'], raw_data['file_paths'], space_comp_pttrn)


if __name__ == '__main__':
    main()