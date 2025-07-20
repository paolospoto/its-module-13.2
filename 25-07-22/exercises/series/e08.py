# Title: Rename Series index
# RULES:
# Change the index labels to 'a', 'b', 'c'

import pandas as pd

s = pd.Series([10, 20, 30])
s.index = ['a', 'b', 'c']
print(s)
