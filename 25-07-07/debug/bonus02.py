# For numbers 1 to 15:
# - Print "Divisible by 3" if divisible by 3
# - Print "Divisible by 5" if divisible by 5
# - Print "Divisible by both" if divisible by both

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by 3")
    elif i % 5 == 0:
        print("Divisible by 5")
    else:
        print(i)
