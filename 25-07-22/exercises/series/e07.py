# Title: Handle missing values
# RULES:
# Create a Series with a missing value (None)
# Replace missing values with 0 using fillna()

import pandas as pd

s = pd.Series([2, None, 3])
filled = s.fillna(0)
print(filled)
