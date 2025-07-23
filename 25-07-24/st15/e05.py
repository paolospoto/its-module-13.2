def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 2 != 0 and numero > 10:
            risultato.append(numero ** 2)
    return risultato
