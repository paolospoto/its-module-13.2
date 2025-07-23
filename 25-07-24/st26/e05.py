def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola.lower().count("l") == 2:
            risultato.append(parola.upper())
    return risultato
