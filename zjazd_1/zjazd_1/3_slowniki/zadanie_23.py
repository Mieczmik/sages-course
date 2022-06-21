# Stwórz funkcje liczącą sume punktów w grze scrabble,
# wykorzystaj poniższy słownik punkow dla danej litery:
values = {'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1, 'l' : 1, 'n' : 1, 'r' : 1, 's' : 1, 't' : 1, 'd' : 2, 'g' : 2,
          'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3, 'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4, 'k' : 5, 'j' : 8, 'x' : 8,
          'q' : 10, 'z' : 10}


print(values.get('a', 0))

def f(D, *args):
    sum = 0
    for key in D.keys():
        sum += D[key]
    return(sum)

print(f(values, 'a', 'z', 'c'))

def count_points(string):
    return sum(values.get(char, 0) for char in string)