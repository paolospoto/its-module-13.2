defaults = {"age": 0}
patient = {"name": "Anna", "info": {"age": 28}}
# patient.update(defaults) => buggy
patient["info"].update(defaults)
print(patient)
print(patient["info"])
