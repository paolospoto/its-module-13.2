words = ["doctor", "dog", "dose"]
prefix = ""

if words:
    for i in range(len(words[0])):
        ch = words[0][i]
        for word in words:
            if word[i] != ch:
                break
        else:
            prefix += ch
else:
    print("No words")

print("Longest common prefix:", prefix)
