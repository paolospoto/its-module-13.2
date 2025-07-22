# Title: Create new column from calculation
# RULES:
# Create a new column "FeelsLike" equal to Temp - 2
import pandas as pd

df = pd.DataFrame({
    "Temp": [36, 38, 37],
    "X": [2, 8, 7]
})

df["Feels Like"] = df["Temp"] - 2

print(df)
