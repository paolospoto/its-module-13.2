# Title: Filtering values
# RULES:
# Print only the values greater than 10.
import pandas as pd

s = pd.Series([3, 66, 9, 12, 15])

print(s[s > 10])
