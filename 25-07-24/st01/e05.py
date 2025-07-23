def unknown_fn(x):
    risultato = []
    for e in x:
        if isinstance(e, int) and e % 3 == 0:
            risultato.append(e ** 2)
    return sorted(risultato, reverse=True)
