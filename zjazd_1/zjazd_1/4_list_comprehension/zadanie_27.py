# Znajdź wszystkie liczby od 10 do 30,
# które zawierają cyfre 3
nowa_lista = list(range(10,31))

def f2(nowa_lista):
        return [elem for elem in nowa_lista if '3' in str(elem)]

print(f2(nowa_lista))

