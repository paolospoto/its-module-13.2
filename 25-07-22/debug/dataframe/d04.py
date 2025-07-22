import pandas as pd

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

# print(df.iloc["0"]) => buggy
print(df.iloc[0])
