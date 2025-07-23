def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola == parola[::-1] and len(parola) > 3:
            risultato.append(parola)
    return risultato
