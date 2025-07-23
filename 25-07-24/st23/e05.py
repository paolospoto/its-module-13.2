def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola.count("a") >= 2:
            risultato.append(parola.upper())
    return risultato
