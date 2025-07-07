# Letter Counter
# RULES:
# - Use a for loop
# - Print only words that contain the letter 'a'

words = ["soccer", "basketball", "tennis", "baseball"]

for w in words:
    if w.count("a") > 0:
        print(w)
