code = input("Enter code: ").strip().upper()

match code:
    case "A01":
        print("Respiratory issue")
    case _:
        print("Unknown code")
