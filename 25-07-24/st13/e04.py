# Il codice dovrebbe costruire una lista con i quadrati dei numeri dispari,
# ma genera una lista sbagliata.

numeri = [1, 2, 3, 4, 5]
quadrati = []
for n in numeri:
    if n % 2 == 1:
        quadrati.append(n * 2)
print(quadrati)
