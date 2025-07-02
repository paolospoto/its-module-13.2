code = input("Enter code: ").strip().upper()

match code   # SyntaxError: missing colon
   case "A01":
        print("Respiratory issue")
    case _:
        print("Unknown code")
