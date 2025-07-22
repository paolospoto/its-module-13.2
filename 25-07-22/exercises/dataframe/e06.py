# Title: Select multiple columns
# RULES:
# Print only the "City" and "Humidity" columns

import pandas as pd

df = pd.DataFrame({
    "City": ["Palermo", "Catania", "Messina"],
    "Humidity": [22, 22, 22],
    "Temp": [36, 38, 39]
})

print(df[["City", "Humidity"]])
