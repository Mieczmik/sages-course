# ZADANIE 16: stwórz funkcję przyjmującą string,
# której wynikiem jest połączenie
# tego napisu ze swoim odbiciem lustrzanym np
# 'pies'->'piesseip

def f(x):
    return x + x[::-1]

print(f('pies'))
