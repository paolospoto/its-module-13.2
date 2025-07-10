#  keys() and values() methods

patient = {"name": "Luca", "age": 30, "temp": 38.2}

# keys() → view of all keys
for key in patient.keys():  # ['name', 'age', 'temp']
    print("Key:", key)

# values() → view of all values
for value in patient.values():  # ['Luca', 30, 38.2]
    print("Value:", value)
