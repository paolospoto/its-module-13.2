# Title: Custom index labels
# RULES:
# Create a Series of 3 temperatures: 36.5, 37.0, 38.2
# Use custom labels: 'morning', 'noon', 'evening'

import pandas as pd

temps = pd.Series([36.5, 37.0, 38.2], index=['morning', 'noon', 'evening'])
print(temps)
