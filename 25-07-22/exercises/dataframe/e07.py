# Title: Sort DataFrame by temperature
# RULES:
# Sort the DataFrame by "Temp" in descending order

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

df_sorted = df.sort_values("Temp", ascending=False)
print(df_sorted)
