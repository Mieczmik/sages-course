def dzielenie(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('nie dziel przez 0')
        print(a/1)
    except TypeError:
        if a.isdigit() or b.isdigit():
            print(int(a)/int(b))
    except Exception:
        print(1)

dzielenie('5', 1)