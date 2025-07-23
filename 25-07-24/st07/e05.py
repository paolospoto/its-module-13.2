def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola[-1] == "o":
            risultato.append(parola[::-1])
    return risultato
