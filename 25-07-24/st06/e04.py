# Il codice dovrebbe restituire una lista di stringhe in minuscolo,
# ma dà un errore o un comportamento inatteso.

parole = ["Ciao", "Python", "Lezione"]
risultato = []
for P in parole:
    risultato.append(P.lowercase())
print(risultato)
