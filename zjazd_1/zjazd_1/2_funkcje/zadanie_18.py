# ZADANIE 18: Napisz funkcję usuwającą znaki specjalne
my_str = "Napis, (ze znakami !) specjalnymi ? %$\n"

def f(my_str):
    lista = [letter for letter in list(my_str) if letter.isalpha() or letter==' ']
    return ''.join(lista)

print(f(my_str))
