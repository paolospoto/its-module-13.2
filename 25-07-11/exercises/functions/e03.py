# Return the average of 3 numbers
# RULES:
# Write a function average(x, y, z) that returns the average of the 3 numbers


def get_avg(x, y, z):
    print("Sto calcolando la media...")
    avg = (x + y + z)/3
    print("Media calcolata, te la restituisco!")
    return avg


print(get_avg(2, 3, 4))
