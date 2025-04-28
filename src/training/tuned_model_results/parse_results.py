"""
- Move detailed checkpoints out of general checkpoint folders if they are present, if they aren't: do not touch
- Read the paths 
- Read the corresponding .json files
- Extract the paths into a .csv file and make them as keys, the values from the .json make as values
"""
from pathlib import Path, PurePath
import shutil
import json

cwd = Path.cwd()

#for child in cwd.iterdir():
    #print(child)

target = Path('temp')

paths = Path('.').rglob('*.json')
for p in paths:
    num_parents = len(p.parents)

    if num_parents > 2:
        stripped_path = "/".join(p.parts[-2:])
        #Path.mkdir(p.parts[-2])
        new_path = Path(".") / stripped_path
        shutil.move(p, new_path)
        
