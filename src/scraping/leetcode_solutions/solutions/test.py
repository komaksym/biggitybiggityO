import re
from pathlib import Path


files_path = 'solutions/'
parsed_data = {'label': [], 'code': []}

def set_regex_pattern(pattern, flags=None):
    return re.compile(rf"{pattern}", flags)


def search_files(folder_path):
    raw_data = []
    for file_path in (Path('.').glob(f'{files_path}/*.py')):
         raw_data.append(file_path.read_text())

    return raw_data


def parse_data(problem_name):
     
    fp = open(f"solutions/{problem_name}")
    file = fp.read()

    code_matches = re.findall(CODES_PATTERN, file)
    label_matches = re.findall(LABELS_PATTERN, file)

    print(f"Num of code matches: {len(code_matches)}")
    print(f"Num of label matches: {len(label_matches)}")

    assert len(code_matches) == len(label_matches)

    for i, (code, label) in enumerate(zip(code_matches, label_matches)):
    
        code = re.sub(FILTER_PATTERN, "", code[0]).strip() 

        print(f"\nSAMPLE
        print("CODE:\n", code, "\n")
        print("LABEL:\n", label, "\n")

        parsed_data['label'].append(label)
        parsed_data['code'].append(code)



CODES_PATTERN = set_regex_pattern(r"(?:
LABELS_PATTERN = set_regex_pattern(r"
FILTER_PATTERN = set_regex_pattern(r"

problem = "find-a-peak-element-ii.py"
parse_data(problem)

#print(parsed_data)
#print(len(parsed_data))
