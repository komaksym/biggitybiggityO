# Time:  O(1)

import pandas as pd


# pandas
def Solution(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
