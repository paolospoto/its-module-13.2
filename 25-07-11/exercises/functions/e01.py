# Greet a patient
# RULES:
# Create a function that takes a name and prints "Hello, [name]"

i = input("What's your name? ")


def say_hello(name=i):
    print("Hello, ", name)


say_hello()
