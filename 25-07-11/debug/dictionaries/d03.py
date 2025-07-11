info = {"temp": 38.1}
# removed = info.pop("weight") => buggy

removed = info.pop("weight", "Nothing to remove")
print("Removed:", removed)
