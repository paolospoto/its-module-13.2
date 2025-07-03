age = int(input("Enter age: "))
# status = "adult" if age >= 18 => buggy
status = "adult" if age >= 18 else 'not adult'

print("Status:", status)
