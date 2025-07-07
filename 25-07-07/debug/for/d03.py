data = [10, 20, 30]

# for i in range(0, len(data) + 1): => buggy
for i in range(0, len(data)):
    print(data[i])
