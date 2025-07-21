# Title: Select multiple columns
# RULES:
# Print only the "City" and "Humidity" columns

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25],
    "Humidity": [60, 70, 65]
})

print(df[["City", "Humidity"]])
