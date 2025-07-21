# Title: Row with maximum value
# RULES:
# Print the row that has the highest temperature

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

max_row = df[df["Temp"] == df["Temp"].max()]
print(max_row)
