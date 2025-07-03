# Remove duplicates
# RULES:
# - Print a list of unique symptoms from a list that may contain duplicates
# TIPS:
# - You can use "not in" to check if an item is in a list
# Example:
# names = ["Alice", "Bob", "Alice", "Charlie"]
# "Paolo" not in names => True

symptoms = ["fever", "cough", "cough", "fever", "pain"]
unique = []

for s in symptoms:
    if s not in unique:
        unique.append(s)

print("Unique symptoms:", unique)
