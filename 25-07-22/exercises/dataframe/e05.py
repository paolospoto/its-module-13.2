# Title: Filter by value
# RULES:
# Print only rows where Temp is greater than 20
import pandas as pd
df = pd.DataFrame({
    "Name": ['Paolo', 'Matteo'],
    "Age": [23, 22],
    "Temp": [36, 17]
})

print(df[df['Temp'] > 20])
