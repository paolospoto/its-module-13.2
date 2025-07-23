def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if "o" in parola and len(parola) < 6:
            risultato.append(parola.upper())
    return risultato
