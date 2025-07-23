# Il codice dovrebbe stampare la media dei numeri nella lista.
# Invece dà errore o un risultato sbagliato.

numeri = [10, 20, 30, 40]
somma = 0
for n in numeri:
    somma = somma + numeri
media = somma / len(numeri)
print("La media è:", media)
