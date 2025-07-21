import pandas as pd

# Q5: What does this return?
# A. Only values greater than 10
# B. A Series of booleans
# C. The max value
# D. An error

s = pd.Series([5, 15, 20])
print(s[s > 10])
