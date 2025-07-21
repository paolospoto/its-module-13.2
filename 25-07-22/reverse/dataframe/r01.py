import pandas as pd


def unknown_fn():
    df = pd.DataFrame({
        "A": [10, 20, 30],
        "B": [1, 2, 3]
    })
    return df["A"] + df["B"]
