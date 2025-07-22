# Title: Count frequency of values
# RULES:
# Count how many times each value appears.
# Use the value_counts() method.
import pandas as pd

s = pd.Series([66, 66, 9, 12, 12, 15, 15])

print(s.value_counts()[66])
