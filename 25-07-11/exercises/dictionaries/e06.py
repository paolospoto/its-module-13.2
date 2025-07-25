# Count occurrences of each symptom in a list
# RULES:
# Build freq dict symptom → count using only dict methods.
# Expected output: # {'cough': 3, 'fever': 2, 'pain': 1}

symptoms = ["cough", "fever", "cough", "pain", "fever", "cough"]

output = {}

for s in symptoms:
    output[s] = output.get(s) + 1

print(output)
