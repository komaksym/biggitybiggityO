# Time:  O(n)

import pandas as pd


# pandas
def Solution(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"],
        value_vars=[f"quarter_{i}" for i in range(1, 4+1)],
        var_name="quarter",
        value_name="sales",
    )
