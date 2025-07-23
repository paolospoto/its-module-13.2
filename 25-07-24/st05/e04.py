# Il codice dovrebbe contare quanti numeri pari ci sono nella lista,
# ma stampa un valore errato.

numeri = [1, 2, 4, 5, 6, 9, 10]
contatore = 0
for numero in numeri:
    if numero % 2 == 0:
        contatore + 1
print("Numeri pari:", contatore)
