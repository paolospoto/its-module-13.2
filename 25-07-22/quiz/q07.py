import pandas as pd

# Q7: What is the correct way to sort by column "Score" descending?
# A. df.sort("Score", ascending=False)
# B. df.sort_values("Score", ascending=False)
# C. df.sortBy("Score", False)
# D. df.Score.sort()

df = pd.DataFrame({
    "Score": [50, 80, 70]
})

df_sorted = df.sort_values("Score", ascending=False)

print(df_sorted)
