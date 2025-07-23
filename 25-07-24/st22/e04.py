# Il codice dovrebbe calcolare la lunghezza media delle parole in una lista,
# ma restituisce risultati errati.

parole = ["ciao", "lezione", "python", "AI"]
totale = 0
for parola in parole:
    totale += parola
media = totale / len(parole)
print("Media:", media)
