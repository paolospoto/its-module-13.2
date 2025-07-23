def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 2 == 0:
            risultato.append(str(numero)[-1])
    return risultato
