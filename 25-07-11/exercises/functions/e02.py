# Temperature checker
# RULES:
# Define a function that takes a temperature and:
# - prints "Normal" if temp < 37.5
# - prints "Fever" if temp >= 37.5

i = float(input("Insert temp: "))


def check_t(temp):
    if temp < 37.5:
        print("Normal")
    else:
        print("Fever")


check_t(i)
