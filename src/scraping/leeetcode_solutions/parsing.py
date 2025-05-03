import re


f = open('solutions/wiggle-sort-ii.py')
file = f.read()

"""
Regex pattern for parsing time complexity labels, 
only what's inside of the brackets, e.g. 'O(n^2)' results in 'n^2'.

We do that by using a non-capturing group and positive lookahead assertion,
which are techniques that are very useful when you want to match your target substring
by using some parts of a string as a guide but you do not want it to be parsed as a result
and so you exclude it, a.k.a. 'not capture' or 'lookahead' (you just look, dont extract)
"""
#labels_pattern = re.compile(r"(?:Time.*?O\()(.*(?=\)))")
#print(re.findall(labels_pattern, file))

"""
Regex pattern for parsing codes

We're matching the codes that start with 'class' continued by
a non-greedy amount of arbitrary symbols, newlines included (hence flag DOTALL)
until we meet a return clause, which is suffixed with a non-greedy amount of symbols
in the same row
"""

labels_pattern = re.compile(r"class.*?return.*?", flags=re.DOTALL)
matches = re.findall(labels_pattern, file)

for m in matches:
    print(m + "\n\n")
