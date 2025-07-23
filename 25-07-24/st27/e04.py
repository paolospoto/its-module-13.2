# Il codice dovrebbe calcolare la somma delle lunghezze delle parole con più di 4 lettere,
# ma restituisce risultati errati.

parole = ["ciao", "lezione", "modulo", "AI"]
totale = 0
for parola in parole:
    if len(parola) > 4:
        totale = len(parola)
print("Totale:", totale)
