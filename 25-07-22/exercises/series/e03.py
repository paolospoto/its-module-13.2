# Title: Access by label and position
# RULES:
# Access the value at position 0
# Access the value with label 'evening'

import pandas as pd

s = pd.Series([100, 200, 300], index=['morning', 'noon', 'evening'])
print(s[0])         # position
print(s['evening'])  # label
