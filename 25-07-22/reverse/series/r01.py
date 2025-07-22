import pandas as pd


def unknown_fn():
    s = pd.Series([3, 7, 5, 12, 9])
    return s[s > 6]


print(unknown_fn())
