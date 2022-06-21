# ZADANIE : Napisz wyrazenie lambda,
# które podniesie kazdy element do potegi 2
lista = [2,3,4]

print([(lambda x: x*x)(x) for x in lista])

print(list(map(lambda x: x*x, lista)))