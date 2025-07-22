import pandas as pd


def unknown_fn():
    s = pd.Series([5, None, 15, None])
    return s.fillna(s.mean())


print(unknown_fn())
