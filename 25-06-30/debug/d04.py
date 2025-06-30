id_number = 123456

# digits = len(id_number) => buggy
digits = len(str(id_number))
print("Digits:", digits)
