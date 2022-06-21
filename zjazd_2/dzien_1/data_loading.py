import pickle

## PLIKI TXT

# f = open("my_file.txt", "w")
# for i in range(10):
#     f.write(f"This is line {i}\n")
# f.close()
#
# f= open("my_file.txt", "r")
# contents= f.read()
# f.close()
# print(type(contents))
# print(contents)

#
# f= open("my_file.txt","w")
# for i in range(10):
#      f.writelines(f"This is line {i}\n")
# f.close()
# #
# f= open("my_file.txt", "r")
# contents = f.readlines()
# for line in contents:
#     print(f'linia : {line}')
# f.close()
#
# with open('my_file.txt', 'r') as my_file :
#     contents = my_file.read()
# # tu juz nie moge np czegos zapisac ani czytac
# print(contents)
# print(my_file.closed)
#
# with open('my_file.txt', 'w') as f :
#     f.write('moj string')

#
# with open('my_file.txt', 'a') as f :
#     f.write('moj string\n')


# with open("my_file.txt","w") as f:
#     for i in range(10):
#          f.writelines(f"This is line {i}\n")

# rozwiazanie z petlą for:
# f= open("my_file.txt", "r")
# contents = f.readlines()
# for line in contents:
#     print(f'linia : {line}')
# f.close()
#
# uzycie petli while
# with open("my_file.txt","r") as f:
#     line = f.readline() #f.readline() reads a single line from the file
#     while line:
#         print(line)
#         line = f.readline()

#
# todo
# # 1. Oblicz ile razy występuje każde imie w pliku 'names.txt'
# oraz wyświetl na ekranie

# with open("dzien_1/data/names.txt", "r") as my_file:
#     contents = my_file.read()
#
# my_list = contents.split()
# [[elem, my_list.count(elem)] for elem in set(my_list)]
# print(my_list)

# todo
# # 2. Znajdź liczby występujące zarówno w pliku numbers_1.txt jak
# i w pliku numbers_2.txt

# with open("dzien_1/data/numbers_1.txt", "r") as my_file:
#     numbers_1 = list(map(int, my_file.read().split()))
#
# with open("dzien_1/data/numbers_2.txt", "r") as my_file:
#     numbers_2 = list(map(int, my_file.read().split()))
#
# [value for value in numbers_1 if value in numbers_2]

#
# ## ENCODE DECODE, CZYLI PROBLEMY Z JĘZYKIEM POLSKIM
# with open('dzien_1/data/polski.txt') as f:
#     line = f.read()
#     print(line)

#
# with open('dzien_1/data/polski.txt', encoding='utf8') as f:
#     line = f.read()
#     print(line)
#
# with open('dzien_1/data/polski.txt', 'r', encoding='windows-1250') as f:
#     line = f.read()
#     print(line)
# #
# with open('dzien_1/data/polski.txt', encoding="ascii") as f:
#     line = f.read()
#     print(line)
#
#
# with open('data/polski_2.txt', 'w', encoding="windows-1250") as f:
#     f.write('Śledź żaden wątły nie jest.')
#
# with open('data/polski_2.txt', 'r', encoding="windows-1250") as f:
#     line = f.read()
#
# print(line)


#
#
# ## PLIKI JSON
# import json

# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

# my_dict = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }
# # # #
# with open("dzien_1/data/my_file_json.json", "w") as f :
#     json.dump(my_dict, f)
# #
# with open("dzien_1/data/my_file_json.json", "r") as f :
#     my_dict = json.load(f)
# #
# print(my_dict['age'] == 35)
# print(type(my_dict['hobbies']))
# print(my_dict['hobbies'][0])
#
# print(my_dict)
#
# import pprint
# pprint.pprint(my_dict)
#
# print(json.dumps(my_dict, indent=4, sort_keys=True))
# https://jsonformatter.curiousconcept.com/
# #
# todo
# # 3. Napisz program podający datę urodzin osób, których nazwiska znajdują się w pliku
# 'birthdays.json'.
# # Program powinien pobierać nazwisko od użytkownika (można to zrobić funkcją 'input').
# # Zaprogramuj również możliwość podania imienia,
# # które nie istnieje na liście oraz możliwość zakończenia programu przez użytkownika.
# print('wpisz imie:')
# name = input()
# print('twoje imie to:', name)
# #
# with open('dzien_1/data/birthdays.json', 'r') as f:
#     birthdays = json.load(f)
#
# for elem in list(birthdays.keys()):
#     if 'Albert' in elem:
#         print(birthdays[elem])

# todo
# # 4. Napisz program zliczający wiek wszystkich superbohaterów
# spisanych w pliku superhero.json.
#
# with open('dzien_1/data/superhero.json', 'r') as f:
#     superhero = json.load(f)
#
# pprint.pprint(superhero)
#
# superhero['members'][0]['age']
#
# age = 0
# for elem in superhero['members']:
#     age = age + int(elem['age'])
# age
#
#
# ## PLIKI PICKLE
#
# import pickle
# #
# my_dict = {
#     "firstName" : "Jane",
#     "lastName" : "Doe",
#     "hobbies" : ["running", "sky diving", "singing"],
#     "age" : 35,
#     "children" : [
#         {
#             "firstName" : "Alice",
#             "age" : 6
#         },
#         {
#             "firstName" : "Bob",
#             "age" : 8
#         }
#     ]
# }
# with open('data/my_file_pickle.pickle', 'wb') as f :
#     pickle.dump(my_dict, f)
#
# with open('data/my_file_pickle.pickle', 'rb') as f:
#     my_dict = pickle.load(f)
# print(my_dict)
#
# # WARNING: https://docs.python.org/3/library/pickle.html