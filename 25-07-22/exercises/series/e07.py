# Title: Handle missing values
# RULES:
# Create a Series with a missing value (None)
# Replace missing values with 0 using fillna()

import pandas as pd

s = pd.Series([100, None, 200, None])
print("Original:")
print(s)

s_filled = s.fillna(0)
print("After fillna:")
print(s_filled)
