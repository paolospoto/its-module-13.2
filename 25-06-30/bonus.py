def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Errore: divisione per zero non consentita.")
        return None
    return a / b


print("=== MINI CALCOLATRICE ===")
num_a = float(input("Primo numero: "))
num_b = float(input("Secondo numero: "))
op = input("Operatore (+  -  *  /): ")

if op == "+":
    result = add(num_a, num_b)
elif op == "-":
    result = subtract(num_a, num_b)
elif op == "*":
    result = multiply(num_a, num_b)
elif op == "/":
    result = divide(num_a, num_b)
else:
    print("Operatore non riconosciuto.")
    result = None

if result is not None:
    print("Risultato =", round(result, 3))
