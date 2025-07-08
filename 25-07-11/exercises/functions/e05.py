# Count how many names start with a vowel
# RULES:
# Write a function that takes a list of names
# and returns how many names start with a vowel (a, e, i, o, u)

def count_vowels(names):
    count = 0
    for name in names:
        if name[0].lower() in "aeiou":
            count += 1
    return count


print(count_vowels(["Anna", "Luca", "Elena", "Marco"]))  # → 2
