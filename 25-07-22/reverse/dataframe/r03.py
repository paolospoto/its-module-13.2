import pandas as pd


def unknown_fn():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Carla"],
        "Age": [25, 30, 28]
    })
    return df.iloc[1]


print(unknown_fn())
