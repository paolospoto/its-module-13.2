import pandas as pd

s = pd.Series([10, 20, 30])
# print(s['1']) => buggy
print(s[1])
