# Il codice dovrebbe contare il numero di parole che iniziano con una lettera maiuscola,
# ma stampa sempre 0.

frasi = ["Oggi è lunedì", "domani piove", "Il corso è utile"]
conta = 0
for frase in frasi:
    parole = frase.split()
    for p in parole:
        if p[0] == p[0].upper():
            conta = conta + 1
        else:
            conta = conta + 0
    conta = 0
print("Maiuscole:", conta)
