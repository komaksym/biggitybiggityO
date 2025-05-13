# Time:  O(1)

import pandas as pd


# pandas
def Solution(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
