# dla podanego stringu policz ilosc wystepowania
# litery 'a'
# (bez użycia .count).
string = 'Ala ma kota i dom'#.lower()
# print(s.count('a'))

def f1(string):
    total = 0
    return [total := total + 1 for letter in string if letter.lower() == 'a'][-1]

print(f1(string))