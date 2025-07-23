def unknown_fn(lista):
    nuova_lista = []
    for n in lista:
        if n < 0:
            nuova_lista.append(-n)
        else:
            nuova_lista.append(n)
    return nuova_lista
