# Count how many names start with a vowel
# RULES:
# Write a function that takes a list of names
# and returns how many names start with a vowel (a, e, i, o, u)

words = ["ciao", "ape", "Matteo", "Elena"]


def count_vowels(ls: list[str]):
    counter = 0
    for word in ls:
        if word[0].lower() in "aeiou":
            counter += 1

    return counter


print(count_vowels(words))
