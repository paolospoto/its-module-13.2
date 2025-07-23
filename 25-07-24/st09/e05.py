def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola[0] == parola[-1]:
            risultato.append(parola)
    return risultato
