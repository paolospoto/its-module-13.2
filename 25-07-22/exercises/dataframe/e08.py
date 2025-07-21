# Title: Create new column from calculation
# RULES:
# Create a new column "FeelsLike" equal to Temp - 2

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

df["FeelsLike"] = df["Temp"] - 2
print(df)