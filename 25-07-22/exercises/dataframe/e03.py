# Title: Access a column
# RULES:
# Print the "Temp" column only
import pandas as pd

df = pd.DataFrame({
    "Name": ['Paolo', 'Matteo'],
    "Age": [23, 22],
    "Temp": [36, 37]
})


print(df['Ciao'])
print("Sono arrivato quaaaaa")
print(df.Ciao)
