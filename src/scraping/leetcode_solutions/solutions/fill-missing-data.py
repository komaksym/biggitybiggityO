# Time:  O(n)

import pandas as pd


# pandas
def Solution(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"].fillna(0, inplace=True)
    return products
