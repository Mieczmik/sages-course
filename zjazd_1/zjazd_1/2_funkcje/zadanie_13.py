# Zadanie 13: Stwórz funkcje tworząca poniższy schemat:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# print('to jest\n koniec linii')

def f(x):
    counter = 0
    while counter <= x:
        print(counter*(str(counter)+' '))
        counter = counter + 1

f(3)


