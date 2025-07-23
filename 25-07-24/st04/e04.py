# Il codice dovrebbe stampare solo le chiavi dei valori maggiori di 5,
# ma stampa risultati sbagliati.

dati = {"a": 3, "b": 7, "c": 2, "d": 9}
for chiave in dati:
    if dati[chiave > 5]:
        print(chiave)
