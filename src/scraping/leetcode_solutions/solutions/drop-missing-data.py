# Time:  O(n)

import pandas as pd


# pandas
def Solution(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=["name"], inplace=True)
    return students
