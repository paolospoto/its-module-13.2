color = input("Enter color: ")

# if color == "red" or "yellow": => buggy
if color == "red" or color == "yellow":
    print("Alert color")
else:
    print("Safe color")
