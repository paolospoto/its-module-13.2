# Temperature warning
# RULES:
# - Use a for loop
# - Print a warning if the temperature is above 38.5°C

temperatures = [36.6, 37.4, 38.2, 39.0, 36.9]

for t in temperatures:
    if t > 38.5:
        print("Warning!")
    else:
        print("T ok")
