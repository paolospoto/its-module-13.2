# Title: Concatenate two Series
# RULES:
# Combine two Series into one
# Reset index using ignore_index=True
import pandas as pd

s = pd.Series([10, 20, 30])

s = s._append(pd.Series([40]), ignore_index=True)

print(s)
