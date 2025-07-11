# Update multiple fields at once
# RULES:
# Add "temp": 37.9 and change "age" to 29

patient = {"name": "Luca", "age": 30}

patient.update({"temp": 37.9, "age": 29})

print(patient)
