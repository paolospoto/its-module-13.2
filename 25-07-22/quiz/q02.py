import pandas as pd

# Q2: How can you select both "Name" and "City" columns from the DataFrame?
# A. df["Name", "City"]
# B. df[["Name", "City"]]
# C. df.Name, df.City
# D. df.select(["Name", "City"])

df = pd.DataFrame({
    "Name": ["Anna", "Luca"],
    "City": ["Rome", "Milan"]
})
