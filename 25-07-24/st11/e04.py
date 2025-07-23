# Il codice dovrebbe stampare il numero più grande della lista,
# ma restituisce un valore errato.

numeri = [5, 17, 3, 22, 9]
massimo = 0
for n in numeri:
    if n > massimo:
        massimo = n
print("Il massimo è:", massimo)
