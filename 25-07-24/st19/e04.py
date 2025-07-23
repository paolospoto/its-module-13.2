# Il codice dovrebbe verificare se almeno una parola ha tutte le lettere in minuscolo,
# ma non funziona correttamente.

parole = ["Python", "debug", "MODULO", "lezione"]
trovata = False
for parola in parole:
    if parola == parola.lower:
        trovata = True
print("Trovata:", trovata)
