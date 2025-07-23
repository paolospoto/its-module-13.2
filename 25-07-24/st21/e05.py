def unknown_fn(lista):
    risultato = []
    for parola in lista:
        if parola[-1] in "aeiou":
            risultato.append(parola.upper())
    return risultato
