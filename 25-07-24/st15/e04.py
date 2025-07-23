# Il codice dovrebbe stampare "OK" se la lista contiene almeno una parola con lunghezza > 5,
# ma non funziona correttamente.

parole = ["ciao", "lezione", "AI"]
ok = False
for parola in parole:
    if len(parola) > 5:
        ok = True
    else:
        ok = False
print("OK" if ok else "NO")
