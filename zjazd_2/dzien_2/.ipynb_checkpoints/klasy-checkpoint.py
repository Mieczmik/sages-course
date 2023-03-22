#!/usr/bin/env python
# coding: utf-8

# # KLASY
# class Dog:
#     def __init__(self):
#         self.name = 'Azor'
#         self.age = 5
# # #
# dog1 = Dog() # funkcja()
# print(dog1.name, dog1.age)
#
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# dog1 = Dog("Azor", 6)
# # #
# print(dog1.name, dog1.age+1)
# dog1.name = 'azor2'
# print(dog1.name)
#
# #


# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def give_voice(self):
#         print("hau hau, my name is {}".format(self.name))
#
#     def add_age(self, numb):
#         self.age +=numb
# # #
# dog1 = Dog("Azor", 5)
# dog1.give_voice()
# dog1.add_age(1)
# print(dog1.age)
#
# #
# dog1.age = 4
# print(dog1.age)
# #
# dog2 = Dog("Burek", 6)
# print(dog2.name, dog2.age)
# #
# dog2.give_voice()
#
# class Dog:
#     def __init__(self, name, age, animal_type='dog'):
#         self.name = name
#         self.age = age
#         self.animal_type = animal_type
# # # #
# #
# dog1 = Dog("Burek", 6)
# print(dog1.name, dog1.age, dog1.animal_type)
# #
# dog1 = Dog("Burek", 6, 'cat')
# print(dog1.name, dog1.age, dog1.animal_type)
# #
# dog1.animal_type = 'dog'
# print(dog1.animal_type)
# #
# dog2 = Dog(5, "Azor")
# print(dog2.name, dog2.age, dog2.animal_type)
#
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def count_age(self, years):
#         self.age = years + self.age
#         print("jestem {}, za {} lat bede mial {} lat".format(self.name, years, self.age))
#
#     def set_age(self, num):
#         self.age +=num
# #
# # #
# dog1 = Dog("Azor", 5)
# dog1.count_age(5)
#
# dog1 = Dog("Azor", 5)
# dog1.count_age(5)


# #
# todo
# 1. Stwórz klase Car, której atrybutami będą kolor, rocznik, cena oraz marka.
# Klasa ta ma posiadać również metodę (funkcję) wyświetlającą w.w. dane,
# z tym, że cena ma byc po przecenie, której procent ma być podawany do
# metody jako zmienna.
# Stwórz dwa obiekty tej klasy i wykonaj na nich metode.

# class Car():
#     def __init__(self, kolor, rocznik, cena, marka):
#         self.kolor = kolor
#         self.rocznik = rocznik
#         self.cena = cena
#         self.marka = marka
#
#     def printer(self, przecena):
#         print(f"Kolor samochodu: {self.kolor}\n"
#               f"Rocznik samochodu: {self.rocznik}\n"
#               f"Cena samochodu po obniżce: {(1 - przecena) * self.cena}\n"
#               f"Marka samochodu: {self.marka}"
#               )
#
#
# Car1 = Car('czerwony', 1997, 6000, 'Toyota')
# Car1.printer(0.2)
#
# Car2 = Car('czarny', 2007, 60000, 'BMW')
# Car2.printer(0.3)

# # ## GENERATORY
#
# # Iterator: by pobrać z niego kolejną wartość, wywołujemy metodę next().
# #
# # Funkcja z generatorem może również zostać wstrzymana oraz wznowiona od
# miejsca, w którym została wstrzymana. Na podstawie zapamiętanego, stanu
# możliwe jest zwracanie różnych wartości podczas kolejnych wstrzymań funkcji.
# #
# # Generatory cechuje leniwa ewaluacja (ang. lazy evaluation), czyli
# tworzenie kolejnych elementów dopiero przy odwołaniu się do generatora.
# Technika ta pozwala zredukować liczbę wykonywanych obliczeń,
# zmniejszyć wykorzystanie pamięci oraz tworzyć nieskończoną ilość elementów.


def liczby():
    for i in range(11):
        yield i * 2
# #
for parzysta in liczby(): #for parzysta in range(11):
    print(parzysta)
    print('ok')
#

def generate_numbers():
    print("rozpoczynam")
    yield (1)
    print("juz byla jedynka")
    yield (2)
    print("juz byla dwojka")
    yield (3)
    yield (4)
    print("zakonczenie generatora")


# #
# generator = generate_numbers()
# print(generator)
# #
# normalna funkcja:
# zmienna = fun()
# dla generatora:
# zmienna = next(generator)

# print('tutaj zwrocil cos: ', next(generator))
# print("drugi raz wywołuje generator")
# print('tutaj zwrocil cos: ', next(generator))
# print("trzeci raz wywołuje generator")
# print('tutaj zwrocil cos: ', next(generator))
# print("czwarty raz wywołuje generator")
# print('tutaj zwrocil cos: ', next(generator))
# #


# PRZYKŁAD Z SESSION (https://docs.sqlalchemy.org/en/13/orm/session_basics.html):
# def session_scope():
#     """Provide a transactional scope around a series of operations."""
#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()


# DZIEDZICZENIE
# class Animal:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#
#     def grow_up(self, age) :
#         self.age += age
# # #
# # #
# class Dog(Animal):
#     def __init__(self, name, age, hair_color, toy) :
#         super().__init__(name, age)
#         self.hair_color = hair_color
#         self.__favourite_toy = toy
#
#     def give_voice(self) :
#         print("hau hau, my name is {}".format(self.name))
# # #
# # #
# class Parrot(Animal) :
#     def __init__(self, name, age, color) :
#         super().__init__(name, age)
#         self.color = color
# # #
# dog1 = Dog('Azor', 5, 'brown', 'bone')
# print(dog1.name, dog1.age)
# dog1.grow_up(2)
# print(dog1.age)
# #
# dog1.__favourite_toy = 'bone2'
# print(dog1.__favourite_toy)
# #
# dog1.give_voice()
#
#
# parrot1 = Parrot('Klara', 8, 'blue')
# print(parrot1.name, parrot1.age, parrot1.color)
# parrot1.grow_up(2)
# print(parrot1.age)

# przyklad kodu z uzyciem klas:
# class DateMonthly:
#     def __init__(self, data):
#         self.delta = datetime.timedelta(seconds=0.000001)
#         self.data = data
#         self.begin_date = self.get_begin_date()
#         self.end_date = self.get_end_date()
#         self.previous_end_date = self.get_previous_end_date()
#
#     def get_begin_date(self):
#         begin_date = datetime.datetime(self.data.year, self.data.month, 1, 0, 0)
#         return begin_date
#
#     def get_end_date(self):
#         end_date = datetime.datetime(self.data.year,
#                                      self.data.month,
#                                      monthrange(self.data.year, self.data.month)[1],
#                                      23,
#                                      59,
#                                      59,
#                                      999999)
#         return end_date
#
#     def get_previous_end_date(self):
#         previous_end_date = self.begin_date - self.delta
#         return previous_end_date
