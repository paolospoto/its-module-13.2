# Title: Access a column
# RULES:
# Print the "Temp" column only

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples"],
    "Temp": [22, 18, 25]
})

print(df["Temp"])
