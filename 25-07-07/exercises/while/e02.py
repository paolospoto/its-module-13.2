# Ask the user until they enter a realistic body temperature
# RULES:
# - Use a while loop
# - Body temperature must be between 34.0 and 42.0 degrees Celsius

bt = int(input("Insert bt: "))

while bt <= 34 or bt >= 42:
    print("Input not valid, try again")
    bt = int(input("Insert bt: "))
