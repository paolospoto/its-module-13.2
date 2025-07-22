import pandas as pd

s = pd.Series([1, 2, 3])
s = s._append(pd.Series([4]), ignore_index=True)
print(s)
