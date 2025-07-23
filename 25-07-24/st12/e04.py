# Il codice dovrebbe stampare "OK" solo se TUTTI i numeri sono maggiori di zero,
# ma stampa "OK" anche se ce ne sono di negativi.

numeri = [3, 5, -2, 9]
ok = True
for n in numeri:
    if n > 0:
        ok = True
print("OK" if ok else "Errore")
