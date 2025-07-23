# Il codice dovrebbe contare quante parole hanno più di 4 lettere,
# ma restituisce un conteggio sbagliato.

parole = ["python", "AI", "debug", "modulo", "dati"]
conta = 0
for p in parole:
    if len(p) > 4:
        conta += 1
    else:
        conta += 0
    conta = 0
print("Parole lunghe:", conta)
