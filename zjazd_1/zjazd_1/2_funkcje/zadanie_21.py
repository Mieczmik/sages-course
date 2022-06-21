# Napisz funkcję , która będzie zwracać sume i
# iloczyn wszystkich podanych argumentów

def f(*args):
    sum = 0
    product = 1
    for i in args:
        sum += i
        product *= i
    return [sum, product]

print(f(1,2,3,4))
