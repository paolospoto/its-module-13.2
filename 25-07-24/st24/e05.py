def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if len(parola) == 4 or parola[0] == "m":
            risultato.append(parola[::-1])
    return risultato
