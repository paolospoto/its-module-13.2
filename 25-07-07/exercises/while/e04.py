# Collect only positive oxygen levels
# RULES:
# - Use a while loop
# - Collect exactly 3 valid oxygen levels
# - If a reading is not > 0, skip it and ask again

oxygen_levels = []

x = float(input("Insert value: "))

while len(oxygen_levels) <= 2:
    if x > 0:
        print("Valid value")
        oxygen_levels.append(x)
        x = float(input("Insert value: "))
    else:
        print("Value not valid")
        x = float(input("Insert value: "))
