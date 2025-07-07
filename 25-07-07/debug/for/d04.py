scores = [4, 5, 6]

total = 0
for s in scores:
    #    total = 0 => buggy
    total += s

print("Total:", total)
