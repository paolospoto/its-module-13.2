# Find word with more "a"
# RULES:
# Use a ternary operator
# - Compare two words and print the one with more vowels
# TIPS:
# - Use the count method to count "a" in each word
# Example:
# word = "hello"
# word.count("l") => 2

first_word = input('Insert first word: ')
second_word = input('Insert second word: ')

result = first_word if first_word.count('a') > second_word.count('a') else (
    'Same number' if first_word.count('a') == second_word.count('a') else second_word)


print(result)
