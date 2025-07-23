def unknown_fn(lista):
    risultato = []
    for elemento in lista:
        if type(elemento) == str and len(elemento) % 3 == 0:
            risultato.append(elemento.lower())
    return risultato
