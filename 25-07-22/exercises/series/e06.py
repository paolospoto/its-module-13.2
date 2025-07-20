# Title: Count frequency of values
# RULES:
# Count how many times each value appears.
# Use the value_counts() method.

import pandas as pd

votes = pd.Series([18, 20, 20, 25, 18, 30, 25])
print(votes.value_counts())
