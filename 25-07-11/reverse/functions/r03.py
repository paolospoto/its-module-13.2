def get_num_of_vowels(text: str) -> int:
    num_of_vowels = 0
    for ch in text.lower():
        if ch in "aeiou":
            num_of_vowels += 1
    return num_of_vowels


print(get_num_of_vowels("Python"))
