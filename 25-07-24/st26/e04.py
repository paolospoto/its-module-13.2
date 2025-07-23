# Il codice dovrebbe contare quante parole contengono almeno 2 vocali,
# ma restituisce un numero errato.

parole = ["ciao", "python", "lezione", "AI"]
conta = 0
for parola in parole:
    vocali = 0
    for lettera in parola:
        if lettera in "aeiou":
            vocali += 1
    if vocali >= 2:
        conta = 0
        conta += 1
print("Trovate:", conta)
