# ZADANIE 4 : Stwórz listę liczb od 1 do 20. Wybierz z
# niej elementy parzyste, jednak nie bierz 10 pod uwagę.
# Nie wypisuj liczb większych niż 13

moja_lista = list(range(1,21))

moja_lista = moja_lista[1::2]
moja_lista.remove(10)




moja_lista = [elem for elem in moja_lista if elem <= 13]
print(moja_lista)



