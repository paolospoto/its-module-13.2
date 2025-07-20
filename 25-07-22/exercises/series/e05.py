# Title: Filtering values
# RULES:
# Print only the values greater than 10.

import pandas as pd

s = pd.Series([5, 12, 9, 20])
filtered = s[s > 10]
print(filtered)
