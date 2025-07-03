age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
    print("Needs supervision")
# print("Needs supervision") => buggy
else:
    print("Adult")
