def unknown_fn(lista):
    risultato = []
    for stringa in lista:
        if len(stringa) >= 4 and "e" in stringa:
            risultato.append(stringa[:2] + "*")
    return risultato
