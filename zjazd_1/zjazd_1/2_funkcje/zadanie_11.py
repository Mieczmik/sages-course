# ZADANIE 11: napisz 2_funkcje przyjmującą string.
# Policz ile razy
# znajduje się słowo "usa", niezależnie od wielości
# liter

zdanie = 'Usa wybory w usa, USA'
wyraz = 'USA'

def f(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    counter = s1.count(s2)
    return print(counter)

f(zdanie, wyraz)




