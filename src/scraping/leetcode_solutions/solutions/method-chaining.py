# Time:  O(nlogn)

import pandas as pd


# pandas
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
     return animals[animals['weight'] > 100].sort_values(by="weight", ascending=False)[['name']]
