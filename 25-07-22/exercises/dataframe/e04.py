# Title: Add new column to DataFrame
# RULES:
# Add a column "Humidity" with 3 values

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

df["Humidity"] = [60, 70, 65]
print(df)
