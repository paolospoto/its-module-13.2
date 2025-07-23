# Il codice dovrebbe creare una lista con il quadrato dei numeri dispari,
# ma restituisce risultati errati.

numeri = [1, 2, 3, 4, 5]
risultato = []
for n in numeri:
    if n % 2 == 1:
        risultato = n * n
print(risultato)
