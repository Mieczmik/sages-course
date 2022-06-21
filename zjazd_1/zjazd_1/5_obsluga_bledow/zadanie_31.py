# Napisz funkcję dzieląca liczby,
# z uwzględnieniem ZeroDivisionError oraz TypeError.
# Jeśli uzytkownik poda ktorąś z liczb większą od
# 100 zwróc jakiś błąd (ValueError). -> raise ValueError
def dzielenie(a,b):
    try:
        if a <= 100 and b <= 100:
            print(a/b)
        else:
            raise ValueError('liczba wieksza niz 100!')

    except ZeroDivisionError:
        print('nie dziel przez 0')
        print(a/1)
    except TypeError:
        if a.isdigit() or b.isdigit():
            print(int(a)/int(b))

dzielenie(100,20)