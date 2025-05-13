# Time:  O(nlogn)

import pandas as pd


# pandas
def Solution(animals: pd.DataFrame) -> pd.DataFrame:
     return animals[animals['weight'] > 100].sort_values(by="weight", ascending=False)[['name']]
