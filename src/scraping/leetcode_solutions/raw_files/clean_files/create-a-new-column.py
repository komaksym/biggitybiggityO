# Time:  O(n)

import pandas as pd


# pandas
def Solution(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=2*employees["salary"])
