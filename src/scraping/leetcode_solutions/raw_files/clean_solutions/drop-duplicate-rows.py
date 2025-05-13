# Time:  O(n)

import pandas as pd


# pandas
def Solution(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=["email"], keep="first", inplace=True)
    return customers
