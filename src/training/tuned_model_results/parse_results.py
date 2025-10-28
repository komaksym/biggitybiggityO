"""
- Read the paths 
- Read the corresponding .json files
- Extract the paths into a .csv file and make them as keys, the values from the .json make as values
"""
from pathlib import Path, PurePath
import shutil
import json
import pdb
import pandas as pd

# Models leaderboard
models_lb = pd.read_csv("models_leaderboard.csv")

# Searching files
paths = Path('.').rglob('*.json')

# Iterating over the files
for p in paths:
    # Parsing the checkpoint
    checkpoint = p.parent

    # Parsing the data
    data = json.loads(p.read_text())

    eval_acc = round(data['eval_accuracy'] * 100, 2)
    eval_f1_macro = round(data['eval_f1_macro'] * 100, 2)
    hc_score = round(data['eval_hierarchy_score'] * 100, 2)

    # Populating the leaderboard
    new_row = {
        'checkpoint': checkpoint,
        'eval_accuracy': eval_acc,
        'eval_f1_macro': eval_f1_macro,
        'eval_hc_score (tltb)': hc_score
    }

    # Add the new row
    new_row = pd.DataFrame([new_row])
    models_lb = pd.concat([models_lb, new_row], ignore_index=True)

# Sort by f1_macro
models_lb.sort_values(by=['eval_f1_macro'], axis=0, ascending=False, inplace=True)

# Save the model leaderboard
models_lb.to_csv("models_leaderboard.csv", index=False)
    
