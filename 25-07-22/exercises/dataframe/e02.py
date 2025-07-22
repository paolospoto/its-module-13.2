# Title: View top of DataFrame
# RULES:
# Use the head() method to display the first two rows
import pandas as pd

df = pd.DataFrame({
    "Name": ['Paolo', 'Matteo', 'Chiara'],
    "Age": [23, 22, 24]
})

print(df.head(2))
