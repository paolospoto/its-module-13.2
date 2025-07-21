# Title: View top of DataFrame
# RULES:
# Use the head() method to display the first two rows

import pandas as pd

df = pd.DataFrame({
    "City": ["Rome", "Milan", "Naples", "Bologna"],
    "Temp": [22, 18, 25, 20]
})

print(df.head(2))
