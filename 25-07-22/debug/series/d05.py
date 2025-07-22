import pandas as pd

s = pd.Series([10, 20, 30], index=[1, 2, 3])
# print(s[0]) => buggy
print(s[1])
