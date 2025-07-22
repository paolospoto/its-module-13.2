import pandas as pd


def unknown_fn():
    s = pd.Series([10, 20, 30])
    s[1] = s[1] * 2
    return s


print(unknown_fn())
