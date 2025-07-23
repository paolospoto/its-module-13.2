# Il codice dovrebbe sommare solo i numeri maggiori di 10,
# ma restituisce un totale sbagliato.

numeri = [5, 12, 20, 7, 15]
totale = 0
for n in numeri:
    if n > 10:
        totale = + n
print("Totale:", totale)
