# Longest common prefix
# RULES:
# - Find and print the longest common prefix among a list of words
# Example: ["doctor", "dog", "dose"] → "do"

words = ["doctor", "dog", "dose"]
prefix = ""

for i in range(len(words[0])):
    current_char = words[0][i]
    for word in words[1:]:
        if i >= len(word) or word[i] != current_char:
            print("Longest common prefix:", prefix)
            break
    else:
        prefix += current_char
        continue
    break
else:
    print("Longest common prefix:", prefix)
