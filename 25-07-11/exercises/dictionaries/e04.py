# Loop over key-value pairs
# RULES:
# Print each key followed by its value

patient = {"name": "Anna", "age": 28, "temp": 37.8}

for key, value in patient.items():
    if key == "age":
        continue
    print(key, "=>", value)
