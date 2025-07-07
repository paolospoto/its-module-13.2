# Waiting List
# RULES:
# - Use a list to manage a waiting list for patients
# - Add three patients to the list then remove the first one in line
waiting_list = []


waiting_list.append("Paolo")
print(waiting_list)
waiting_list.append("Matteo")
waiting_list.append("Riccardo")

print(waiting_list)

name = waiting_list.pop(0)

print(waiting_list)
print(name)
