import re
import pdb


TEXT = """
# Time:  'dsfdfO('(n * m)

# Time:  ctor:    O(1)
#        upload:  O(1), amortized
#        longest: O(1)


# Time:  "dsfdf O("(n * m)

# Time:  O((logn)^2)

# Time:  O (n * k), k = max(cnt for _, cnt in requirements)

# Time:  O(n * sqrt(n)) = O(n^(3/2))

# Time:  O   (s1 * min(s2, n1))

# Time:  O  (n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time

# Time:  precompute: O(max_n^2 + max_y * min(max_n, max_x))
#        runtime:    O(min(n, x))

# Time:  O(logn)

# Time:  O(n^2 * n!)


--------------------------------------------------------------------------

import math


class Solution(object):
    def arrangeCoins(self, n):
        return int((math.sqrt(8*n+1)-1) / 2)  # sqrt is O(logn) time.


# Time:  ctor:         O(nlogn)
#        changeRating: O(logn)
#        highestRated: O(1)

# Time:  ctor:         Oa(nlogn)
#        changeRating: fO(logn)
#        highestRated: do(1)

class Solution2(object):
    def arrangeCoinsO(self, n):
        def check(mid, n):
            return mid*(mid+1) <= 2*n

        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid, n):
                right = mid-1
            else:
                left = mid+1
        return right
"""


def extract_O_blocks(text):
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

matches = extract_O_blocks(TEXT)
print(matches)
print(len(matches))



















#import re
#from pathlib import Path
#import pdb
#
#
#files_path = 'solutions/'
#parsed_data = {'label': [], 'code': []}
#corrupted_data = []
#
#
#def set_regex_pattern(pattern, flags=0):
#    return re.compile(rf"{pattern}", flags)
#
#
#def search_files(folder_path):
#    raw_data = {'file_paths': [], 'files': []}
#
#    for file_path in (Path('.').glob(f'{files_path}/*.py')):
#         raw_data['file_paths'].append(file_path)
#         raw_data['files'].append(file_path.read_text())
#
#    return raw_data
#
#
#def parse_data(files_path, files, pattern):
#    total_matches = 0
#
#    for path, file in zip(files_path, files): 
#        matches = re.findall(pattern, file)
#
#        total_matches += len(matches)
#
#        for m in matches:
#            print(m)
#
#    print(f"Num of total matches: {total_matches}")
#
#
#pattern = set_regex_pattern(r"\bO\b\(")
#
#raw_data = search_files(files_path)
#parse_data(raw_data['file_paths'], raw_data['files'], pattern)