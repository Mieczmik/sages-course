# stworz funkcje sumująca wszystkie argumenty,
# które sa podzielne przez 3 ale mniejsze od 20 w
# poniższej liście

# print([num+1 for num in moja_lista])
# print([num+1 for num in moja_lista if num>1])
# print([True if num>1 and num<3 else False for num in moja_lista ])
#
lista = [22, 36, 3, 9, 5, 6, 66]

def f1(lista):
    return sum([x for x in lista if (x % 3 == 0 and x < 20)])

def f2(lista):
    total = 0
    return [total := total + x for x in lista if (x % 3 == 0 and x < 20)][-1]


print(f1(lista))
print(f2(lista))
