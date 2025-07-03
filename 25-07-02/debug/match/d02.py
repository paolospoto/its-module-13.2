level = input("Enter alert level: ").strip().lower()

match level:
    # case "red" or "orange": => buggy
    case "red" | "orange":
        print("High alert")
    case _:
        print("Normal")
