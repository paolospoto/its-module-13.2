def unknown_fn(lista):
    risultato = []
    for parola in lista:
        nuova = parola.replace("e", "*")
        if len(nuova) >= 5:
            risultato.append(nuova)
    return risultato
