# Hospital fever report (simplified)
# RULES:
# 1. Patient records are stored in a nested dictionary:
#    id → {"name": str, "temp": float}
# 2. Build a report dict called report with:
#    • "highest_temp": the highest temperature recorded
#    • "patient_id":   the id of the patient with that highest temp
#    • "fever_patients": list of dictionaries with name and temp keys of all patients with temp ≥ 38.0
# 4. Print report at the end

patients = {
    "P001": {"name": "Anna",  "temp": 37.8},
    "P002": {"name": "Luca",  "temp": 38.2},
    "P003": {"name": "Elena", "temp": 36.9},
    "P004": {"name": "Emanuele", "temp": 38.0},
}


record = {
    'highest_temp': 0,
    'patient_id': None,
    'fever_patients': []
}
