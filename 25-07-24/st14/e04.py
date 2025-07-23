# Il codice dovrebbe contare il numero di vocali in una stringa,
# ma restituisce un valore sbagliato.

testo = "lezione di programmazione"
vocali = "aeiou"
conta = 0
for c in testo:
    if c in vocali:
        conta = conta + 1
    else:
        conta = 0
print("Numero di vocali:", conta)
