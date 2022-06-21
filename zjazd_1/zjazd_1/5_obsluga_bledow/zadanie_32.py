# Popraw poniszy kod wykorzystując:
# ZeroDivisionError, ValueError, IndexError, TypeError.
def example1():
    x = int(input("enter a number: "))
    y = int(input("enter another number: "))
    try:
        print(x / y)
    except ZeroDivisionError:
        'Nie dziel przez 0.'
    except ValueError:
        'ValueError'
    except IndexError:
        'IndexError'
    except TypeError:
        print(int(x) / int(y))


#example1()

def example2(lista):
    suma = []
    try:
        for i in range(len(lista)):
            suma.append(lista[i] + lista[i + 1])
            print(suma)
    except ZeroDivisionError:
        'Nie dziel przez 0.'
    except ValueError:
        'ValueError'
    except IndexError:
        'IndexError'
    except TypeError:
        print('Podales stringa')


print(example2([1,2]))