answer = input("Continue? (y / yes): ").strip().lower()
# proceed = answer == "y" or "yes" => buggy
proceed = answer == "y" or answer == "yes"
print("Proceed:", proceed)
