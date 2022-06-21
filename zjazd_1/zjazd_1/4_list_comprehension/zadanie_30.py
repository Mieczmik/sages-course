# napisz formułe, która z dwóch list wybierze
# element większy:

print(max([1,2,3]))
print(sum([1,2,3]))

lista_1 = [1, 20, 30]
lista_2 = [10, 1, 40]

def f(lista_1, lista_2):
    return [max(x, y) for x,y in zip(lista_1, lista_2)]

print(f(lista_1, lista_2))
