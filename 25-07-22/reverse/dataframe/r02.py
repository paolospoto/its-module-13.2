import pandas as pd


def unknown_fn():
    df = pd.DataFrame({
        "City": ["Rome", "Milan", "Naples"],
        "Temp": [22, 18, 25]
    })
    return df[df["Temp"] >= 20]


print(unknown_fn())
