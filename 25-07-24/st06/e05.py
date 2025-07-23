def unknown_fn(lista):
    risultato = []
    for numero in lista:
        if numero % 5 == 0:
            risultato.append(str(numero))
    return "-".join(risultato)
