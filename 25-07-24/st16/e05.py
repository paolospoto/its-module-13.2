def unknown_fn(lista):
    risultato = []
    for stringa in lista:
        if " " in stringa:
            risultato.append(stringa.split()[0])
    return risultato
