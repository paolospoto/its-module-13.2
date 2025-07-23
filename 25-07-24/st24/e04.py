# Il codice dovrebbe trovare la parola più lunga nella lista,
# ma restituisce sempre l’ultima o sbaglia.

parole = ["ciao", "lezione", "debug", "modulo"]
lunga = ""
for p in parole:
    if len(p) > len(lunga):
        lunga = p
    else:
        lunga = p
print("Parola più lunga:", lunga)
