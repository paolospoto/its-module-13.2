matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

col_sums = [0, 0, 0]

for row in matrix:
    for col in range(len(row)):
        col_sums[col] += matrix[0][col]

print("Column sums:", col_sums)
