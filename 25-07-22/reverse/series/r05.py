import pandas as pd


def unknown_fn():
    s = pd.Series([10, 20, 30])
    return s * s


print(unknown_fn())
