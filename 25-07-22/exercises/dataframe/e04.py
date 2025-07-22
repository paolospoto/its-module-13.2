# Title: Add new column to DataFrame
# RULES:
# Add a column "Humidity" with 3 values
import pandas as pd
df = pd.DataFrame({
    "Name": ['Paolo', 'Matteo'],
    "Age": [23, 22],
    "Temp": [36, 37]
})

df['Humidity'] = [2, 3]

print(df)
