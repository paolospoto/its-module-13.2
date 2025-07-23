def unknown_fn(lista):
    risultato = []
    for n in lista:
        if n > 0:
            risultato.append(n * -1)
        else:
            risultato.append(n)
    return risultato
