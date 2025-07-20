import pandas as pd


def unknown_fn():
    s = pd.Series([3, 6, 9, 12])
    return s.mean() > 8
