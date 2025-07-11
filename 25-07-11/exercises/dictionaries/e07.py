# Flatten nested patient temps into one list
# RULES:
# patients dict: id → inner dict with "temp"
# Collect all temps into temps list (order not important).

patients = {
    "P1": {"temp": 37.8},
    "P2": {"temp": 38.5},
    "P4": {"tep": 36.9},
    "P3": {"temp": 36.9},
}

temps = []

for p in patients.values():
    temps.append(p.get("temp", "Temp non disponibile"))

print(temps)
