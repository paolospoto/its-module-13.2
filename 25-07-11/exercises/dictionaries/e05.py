# Find the key with the highest value
# RULES:
# From scores dict (name → score) print the name of the top scorer.

scores = {"Anna": 88, "Luca": 92, "Elena": 91}


highest = 0
name = ""
for key, value in scores.items():
    if value > highest:
        highest = value
        name = key

print(name)
print(highest)
