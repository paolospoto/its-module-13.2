import pandas as pd

# Q1: Which line correctly accesses the "Age" column as a Series?
# A. df.Age()
# B. df["Age"]
# C. df[["Age"]]


df = pd.DataFrame({
    "Name": ["Anna", "Luca"],
    "Age": [22, 30]
})

print(df["Age"])
