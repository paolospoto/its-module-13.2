def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 2 == 0 and numero % 3 == 0:
            risultato.append(numero)
    return risultato
