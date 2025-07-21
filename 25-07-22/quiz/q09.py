import pandas as pd

# Q8: What does value_counts() do?
# A. Returns max value
# B. Counts how often each value appears
# C. Returns the length of the Series
# D. Sorts the values

s = pd.Series([1, 2, 2, 3, 1, 1])

print(s.value_counts())
