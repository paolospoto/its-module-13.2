# Add a symptom to a list (optional urgency)
# RULES:
# Create a function add_symptom(symptoms, symptom, urgent=False)
# - If urgent is True → insert at beginning
# - Otherwise → append at the end

patient_symptoms = ["cough"]


def add_s(symptoms, symptom, urgent=False):
    if urgent:
        symptoms.insert(0, symptom)
    else:
        symptoms.append(symptom)


add_s(patient_symptoms, "fever")
print(patient_symptoms)
add_s(patient_symptoms, "blood", True)
print(patient_symptoms)
