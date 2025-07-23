def unknown_fn(lista):
    nuova = []
    for parola in lista:
        if len(parola) % 2 == 0:
            nuova.append(parola + parola)
    return nuova
