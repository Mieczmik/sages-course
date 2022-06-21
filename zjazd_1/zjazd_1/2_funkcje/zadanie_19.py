# ZADANIE DODATKOWE 19: Napisz 2_funkcje,
# ktorej zadaniem będzie dodanie dwóch macierzy:
# => [17, 15, 4]
# [10, 12, 9]
# [11, 13, 18]

X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

# print(X[1][1])

# Z = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         Z[i][j] = X[i][j] + Y[i][j]

def dodawanie_macierzy(X, Y):
    Z = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
    return Z

print(dodawanie_macierzy(X, Y))