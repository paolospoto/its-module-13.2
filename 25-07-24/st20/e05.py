def unknown_fn(lista):
    risultato = []
    for elemento in lista:
        if elemento.startswith("p") and len(elemento) > 5:
            risultato.append(elemento.upper())
    return risultato
