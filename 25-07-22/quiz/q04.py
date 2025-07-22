import pandas as pd

# Q4: How do you create a new column "C" as the sum of "A" and "B"?
# A. df["C"] = df.A + df.B
# B. df["C"] = df["A" + "B"]
# C. df["C"] = df["A"] + df["B"]
# D. A and C

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})
df["C"] = df.A + df.B
print(df)
