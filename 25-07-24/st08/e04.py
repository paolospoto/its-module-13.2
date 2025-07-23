# Il codice dovrebbe stampare tutti i numeri della lista che sono multipli di 4,
# ma il controllo è sbagliato e il risultato non è corretto.

numeri = [4, 8, 15, 16, 23, 42]
for n in numeri:
    if 4 % n == 0:
        print(n)
