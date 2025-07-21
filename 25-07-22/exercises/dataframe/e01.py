# Title: Basic DataFrame creation
# RULES:
# Create a DataFrame with two columns: "Name" and "Age"
# Add 3 rows with any names and ages

import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Luca", "Marta"],
    "Age": [22, 30, 27]
})
print(df)
