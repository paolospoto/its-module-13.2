# Minutes → hh:mm
total = int(input("Inserisci minuti: "))

hours = total // 60
minutes = total % 60


print("Risultato: ", str(hours).zfill(2), ":", str(minutes).zfill(2))
