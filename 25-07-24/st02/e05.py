def unknown_fn(lista):
    risultato = []
    for elemento in lista:
        if len(elemento) > 4:
            risultato.append(elemento[:3])
    return risultato
