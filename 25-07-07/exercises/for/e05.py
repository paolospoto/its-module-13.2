# Every other patient
# RULES:
# - Use a for loop
# - Print the name of every other patient in the waiting list

waiting_list = ["Luca", "Anna", "Marco", "Sofia", "Gianni"]

for i in range(0, len(waiting_list)):
    if i % 2 != 0:
        print(waiting_list[i])
