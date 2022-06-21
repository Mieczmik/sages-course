# Mając zbiór danych z zadania 5,stwórz 2_funkcje, które:
wysokosci= [829, 632, 601,599.3,554.5 ]
liczba_pieter = [163, 128,120,115,123]
miejsca = ['Dubaj, Zjednoczone Emiraty Arabskie','Szanghaj, Chiny','Mekka, Arabia Saudyjska', 'Shenzhen, Chiny', 'Seul, Korea Południowa']
nazwy = ['Burj Khalifa','Shanghai Tower','Abradż al-Bajt','Ping An Finance Centern','Lotte World Tower']


# - stworzy słownik nazwa: (wysokosc, liczba_pieter)
# np {'Burj Khalifa':(829, 163)}

def stworzslownik(nazwy, wysokosci, liczba_pieter):
    lista = []
    for x, y in zip(wysokosci, liczba_pieter):
        lista.append((x, y))
    D = dict(zip(nazwy, lista))
    return D

def create_dict():
    slownik = dict()
    for naz, wys, lp in zip(nazwy, wysokosci, liczba_pieter):
        slownik[naz] = (wys, lp)
    return slownik

D = stworzslownik(nazwy, wysokosci, liczba_pieter)



# - pozwoli dodawac rekordy do slownika
# (user podaje wszystkie wartosci)

def dodajrekord(D, miejsce, *args):
    D[miejsce] = tuple(args)[:1]

dodajrekord(D, 'Warsaw', 123, 60)

print(D)

# - bedzie usuwac rekordy ze słownika po kluczu

def usunrekord(D, miejsce):
    del D[miejsce]

usunrekord(D, 'Warsaw')

print(D)


# - bedzie zwracac uzytkownikowi,
# czy dany klucz znajduje sie w słowniku
# i czy posiada podana przez uzytkownika wysokosc
# np ('Burj Khalifa', 600) -> False

def keyinfo(D, miejsce, czywysokosc):
    value = D.get(miejsce, 'W slowniku nie ma podanej wartosci')[0]
    return (miejsce, value == czywysokosc)

print(keyinfo(D, 'Burj Khalifa', 600))



# - policzy srednią ilosc pieter wszystkich
# budynkow w slowniku

def srednialiczbapieter(D):
    value = sum(D[key][1] for key in D) / (len(D))
    return value

print(srednialiczbapieter(D))