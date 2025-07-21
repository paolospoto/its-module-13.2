import pandas as pd

def unknown_fn():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })
    df["C"] = df["A"] * 10
    return df
