# Add a missing key with a default value
# RULES:
# 1) Read "weight" safely setting default to 0
# 2) If weight is 0, set patient["weight"] = 70

patient = {"name": "Mario", "age": 28}

w = patient.get("weight")

if w == None:
    patient.update({'weight': 70})
print("P: ", patient)
