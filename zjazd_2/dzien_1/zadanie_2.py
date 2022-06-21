# todo
# W pliku 'pytest.ini' znajduje się kilka sekcji, a każda sekcja zaczyna się od wyrażenia
# w nawiasach kwadratowych []. Wewnątrz każdej sekcji znajdują się pary klucz-wartość
# z opcjonalnymi spacjami koło znaku "=". Klucze mogą zawierać litery, numery, podkreślniki
# (tzw. podłoga "_") lub myślniki. Dodatkowo w pliku mogą znajdować się puste linie oraz
# linie komentarzy, rozpoczynające się od "#". Przekształć plik 'pytest.ini' do poniższej formy:
# $VAR1 = { 'earth' => { 'base' => 'London', 'ship' => 'x-wing' },
# 'alpha' => { 'base' => 'moon', 'ship' => 'alpha 3' } }

import re

try:
    with open("dzien_1/data/pytest.ini") as f:
        contents = f.read().replace(" ", "")
except:
    with open("data/pytest.ini") as f:
        contents = f.read().replace(" ", "")

contents = contents.split("[")
contents = [elem for elem in contents if "]" in elem]

my_dict = {re.search(r'.*[\]]', elem).group()[:-1] : re.findall(r"\S.*[=]\S.*", elem) for elem in contents}
for key, val in my_dict.items():
    new_val = {elem.split("=")[0]: elem.split("=")[1] for elem in val}
    my_dict[key] = new_val

print(my_dict)

# Rozwiązanie Oliwii
# with open('data/pytest.ini', 'r') as f:
#     linie = f.readlines()
#
# dictionary = dict()
#
# for linia in linie:
#     if linia.strip():
#         if '#' not in linia:
#             if '[' in linia:
#                 new_key = linia.replace('[', '').replace(']', '').strip()
#             else:
#                 k, v = linia.split('=')
#                 k = k.strip()
#                 v = v.strip()
#
#             if new_key not in dictionary:
#                 dictionary[new_key] = list()
#             else:
#                 dictionary[new_key].append({k: v})
#
# new_lines = str(dictionary).replace(':', "=>").replace('[', '').replace(']', '')
# print("$VAR1 = "+ new_lines )