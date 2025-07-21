import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Luca", "Marta"],
    "Age": [22, 30, 27]
})

print(df[df["Age"] > 25]["Nome"])
