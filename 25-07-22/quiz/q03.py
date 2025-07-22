import pandas as pd

# Q3: How do you access the second row of the DataFrame?
# A. df.loc[1]
# B. df.iloc[1]
# C. df[1]
# D. df.row(1)

df = pd.DataFrame({
    "A": [10, 20, 30]
}, index=["a", "b", "c"])
