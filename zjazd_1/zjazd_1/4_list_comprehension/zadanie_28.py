# Usun wszystkie samogloski z napisu
napis = "Ala ma Kota i dom" #-> "l m Kt  dm"
lista_samoglosek = 'aeiouAEIOU'

def f(napis, lista_samoglosek):
    lista = [char for char in list(napis) if char not in list(lista_samoglosek)]
    return ''.join(lista)

print(f(napis, lista_samoglosek))