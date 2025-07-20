# Title: Concatenate two Series
# RULES:
# Combine two Series into one
# Reset index using ignore_index=True

import pandas as pd

s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])

combined = pd.concat([s1, s2], ignore_index=True)
print(combined)
