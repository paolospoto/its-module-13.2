symptom = input("Do you have a cough? (y/n): ")

if symptom == "y":
    print("Patient has a cough.")
else:
    # if symptom == "n": => buggy
    if symptom == "n":
        print("Patient does not have a cough.")
