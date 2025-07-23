def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 10 == 0:
            risultato.append(numero // 10)
    return risultato
