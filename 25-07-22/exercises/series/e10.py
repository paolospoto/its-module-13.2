# Title: Filter and update values
# RULES:
# Filter values greater than 50 and multiply them by 2
# Tip: use boolean indexing and assignment

import pandas as pd

s = pd.Series([52, 8, 80])

s[s > 50] = s[s > 50] * 2

print(s)
