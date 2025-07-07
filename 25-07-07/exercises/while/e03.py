# Count how many patients are entered
# RULES:
# - Use a while loop
# - Count the number of patients entered until the user types "stop"

counter = 0

patient = input("Insert name: ")

while patient != "stop":
    counter += 1
    patient = input("Insert name: ")

print(counter)
