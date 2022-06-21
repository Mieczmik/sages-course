# Zadanie 14: Napisz kalkulator (suma, odejmowanie, mnożenie,
# dzielenie)
# dla dwóch liczb, sprawdź, czy użytkownik podaje odpowiednie
# typy danych
# i czy nie chce dzielić przez zero
# mn = mnozenie
# dz = dzielenie
# od - odejmowanie
# do - dodawania

def calc(a, b, c):
    if c == 'mn':
        return a*b
    elif c == 'dz':
        if c==0:
            return 'ehhh'
        else:
            return a/b
    elif c == 'od':
        return a-b
    elif c == 'do':
        return a+b

print(calc(1,4,'dz'))
