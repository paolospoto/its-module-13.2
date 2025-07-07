# Code validation
# RULES:
# - Use a for loop
# - Push codes to a list if they are valid
# - Valid codes must be more than 3 characters long

raw_codes = ["AB1234", "C03", "123456", "XX9", "PQ7890"]
valid_codes = []

for raw in raw_codes:
    if len(raw) > 3:
        print("Valid code:", raw)
        valid_codes.append(raw)

print(valid_codes)
