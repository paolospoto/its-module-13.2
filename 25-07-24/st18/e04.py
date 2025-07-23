# Il codice dovrebbe creare una lista con i primi caratteri di ogni parola nella frase,
# ma restituisce un errore o valori errati.

frase = "corso python debug modulo"
iniziali = []
for parola in frase:
    iniziali.append(parola[0])
print(iniziali)
