def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 4 == 0:
            risultato.append(str(numero))
    return ",".join(risultato)
