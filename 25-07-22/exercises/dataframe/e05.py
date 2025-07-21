# Title: Filter by value
# RULES:
# Print only rows where Temp is greater than 20

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

print(df[df["Temp"] > 20])
