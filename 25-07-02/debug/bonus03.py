# For numbers 1 to 15:
# - Print "Fizz" if divisible by 3
# - Print "Buzz" if divisible by 5
# - Print "FizzBuzz" if divisible by both

for i in range(1, 16):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
