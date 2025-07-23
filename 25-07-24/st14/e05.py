def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola.count("i") == 1:
            risultato.append(parola[::-1])
    return risultato
