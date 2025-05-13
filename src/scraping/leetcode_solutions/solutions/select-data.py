# Time:  O(n)

import pandas as pd


# pandas
def Solution(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]
