import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [1, 2, 3]
})

df["C"] = df["A"] + df["B"]
print(df)
