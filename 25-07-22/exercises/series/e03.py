# Title: Access by label and position
# RULES:
# Access the value at position 0
# Access the value with label 'evening'

import pandas as pd

s = pd.Series([36.5, 37.0, 38.2], index=['morning', 'noon', 'evening'])

print(s['morning'])
print(s[1])
