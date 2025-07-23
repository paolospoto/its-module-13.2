# Il codice dovrebbe stampare "Trovato!" se almeno un numero nella lista è maggiore di 100,
# ma non funziona correttamente.

numeri = [10, 45, 78, 105, 60]
for n in numeri:
    if n > 100:
        trovato = True
    else:
        trovato = False
print("Trovato!" if trovato else "Non trovato.")
