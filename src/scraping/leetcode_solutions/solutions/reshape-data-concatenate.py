# Time:  O(n + m)

import pandas as pd


# pandas
def Solution(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
