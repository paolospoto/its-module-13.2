# Title: Drop a column
# RULES:
# Remove the column "Humidity" from the DataFrame

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25],
    "Humidity": [60, 70, 65]
})

df = df.drop(columns=["Humidity"])
print(df)
