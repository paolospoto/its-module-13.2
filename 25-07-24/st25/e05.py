def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 2 == 0 and str(numero).endswith("2"):
            risultato.append(numero)
    return risultato
