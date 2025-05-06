# Time:  O(n)

import pandas as pd


# pandas
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({"grade" : int})
