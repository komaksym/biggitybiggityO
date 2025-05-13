# Time:  O(n)

import pandas as pd


# pandas
def Solution(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")
