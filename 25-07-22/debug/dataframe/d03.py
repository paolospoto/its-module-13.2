import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan"],
    "Temp": [22, 18],
    "X": [1, 2]
})

# print(df["City", "Temp"]) => buggy
print(df[["City", "Temp"]])
