# Remove a key safely
# RULES:
# Pop "temp" from the dict; store the value in variable t
# If the key is missing, t should be None (no error)

record = {"name": "Elena", }


t = record.pop("temp", None)


print(t)
print(record)
