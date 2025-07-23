# Il codice dovrebbe restituire la lunghezza della parola più corta,
# ma stampa sempre la lunghezza dell’ultima.

parole = ["ciao", "lezione", "modulo", "AI"]
minimo = 999
for parola in parole:
    if len(parola) < minimo:
        minimo = len(parola)
    else:
        minimo = len(parola)
print("Lunghezza minima:", minimo)
