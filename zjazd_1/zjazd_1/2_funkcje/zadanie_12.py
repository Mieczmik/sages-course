# ZADANIE 12: Stwórz funkcję przyjmującą zbiór liczb
# od 1 do 10,
# która dla każdego elementu listy będzie wyświetlała
# sume elementu
# i poprzednich elementów

lista = [1,10,100, 3]

def count_sum(lista):
   suma = 0
   for elem in lista:
        if not(elem>10 or elem<1):
            suma += elem
            print(suma)

count_sum(lista)