# ZADANIE DODATKOWE 20: Napisz 2_funkcje do
# transpozycji macierzy:
X = [[12,7],
    [4 ,5],
    [3 ,8]]
# => [12, 4, 3]
# [7, 5, 8]

def transpozycja_macierzy(X):
    Z = [[X[j][i]  for j in range(len(X))] for i in range(len(X[0]))]
    return Z

print(transpozycja_macierzy(X))