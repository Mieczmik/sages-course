# # REGEX - wyrażenia regularne
import re

# importowanie modulow
# from tests import test_count
# from tests.test_count import sum_num

# test_count.sum_num(1,2)
# sum_num(1,)

#
# print('\tTekst\n')
# print(r'\tTekst')
#
# Funkcja match() zwraca znaleziony napis, jeśli od początku pasuje do patternu. W innym przypadku zwróci None.
# pattern = r"napis"
# sequence = "napis tu jest napisany"
# print(re.match(pattern, sequence))
#
#
# pattern = r"napis"
# sequence = "napis tu jest napisany"
# print(re.match(pattern, sequence).group())

# pattern = r"78"
# sequence = "napis tu jest napisany"
# if_match = re.match(pattern, sequence)
# if if_match:
#     print(re.match(pattern, sequence).group())
#
#
# # search() w przeciwieństwie do match szuka patternu w całym stringu
#
# moj_regex = re.compile(r'ma')
# print(re.search(moj_regex, 'Ala ma kota'))
# print(re.search(moj_regex, 'mama ma kota'))


# pattern = r"napis"
# sequence = "To taki napis"
# print(re.search(pattern, sequence).group())
#
#
# pattern = r"n\."
# zwykly_napis_1 = "napis"
# zwykly_napis_2 = "n23"
# print(re.search(pattern, zwykly_napis_1))
# print(re.search(pattern, zwykly_napis_2))
#
# # Kropka oznacza dowolny znak, oprócz znaku nowej linii
#
# print(re.search(r'N.p.s', 'Napis'))
# print(re.search(r'N.p.s', 'ala ma kota Nop5s'))

# ^ oznacza początek napisu
# print(re.search(r'^Na.', 'Napis ala ma kota').group())
# print(re.search(r'^Na.', 'Na? jj Nal').group())
#
# # $ oznacza koniec napisu
#
# print(re.search(r'Na.$', 'Napis'))
# print(re.search(r'Na.$', 'isNap'))

# # \* powtarza ostatni znak zero lub wiele razy
# print(re.search(r'^Na.*', 'Napis').group())
# print(re.search(r'^Na.*', 'Na').group())
# print(re.search(r'^Na.*', 'Napis ma kota').group())

#
# # \+ powtarza ostatni znak przynajmniej raz
#
# print(re.search(r'Na.*', 'Na'))
# print(re.search(r'Na.+', 'Na'))
# print(re.search(r'Na.+', 'Napppp222????!!%%%'))

#
# # Czasem możemy chcieć zawęzić zakres np w przypadku szukania takiego wzorca:
# # (.*) w takim stringu
# #
# # "(a) b (c)"
# #
# #  zostanie znalezione
# #
# #  "(a) b (c)"
# #
# #  zamiast jedynie
# #
# #  (a)
# #
# # ? w skrócie ogranicza zakres do jak najmniejszego
#
# print(re.search(r'Na*?', 'Naaaaa'))  # zero lub wiele
# print(re.search(r'Na*', 'Naaaaa'))
# print('\n')
# print(re.search(r'a+?', 'Naaaaa'))  # mimum jeden
# print(re.search(r'a+', 'Naaaaa'))
#
# # Jeśli natomiast chcemy wykorzystać poznane powyżej symbole dla większej grupy znaków to możemy zgrupować je w
# # [ ] i następnie użyć któregoś z symbolu lub symboli
#
# print(re.search(r'[lj*?]+', '?h*fjalafelhh?*'))
# print(re.search(r'[lj*?]+', '?jllj*h*fjalafelhh?*'))
# print(re.search(r'[abc]', 'falabac'))
# print(re.search(r'[alh]+', 'lahla'))

# print(re.search(r'[a-c]', 'bfalabac'))
# print(re.search(r'\d+', '123456778'))
# print(re.search(r'ala \b', 'alamakota ma kota ala'))
#
# # Istnieją też skróty, które pozwalają nam wyszukiwać grupy znaków szybciej
# #
# #     * \d - cyfry == [0-9]
# #     * \D - nie cyfry
# #     * \s - spacje, taby, nowe linie itp
# #     * \S - stringi, włączając w to znaki specjalne oraz cyfry
# #     * \w - słowa + cyfry, czyli j.w. bez znaków specjalnych [a-zA-Z0-9_]
# #     * \W - zaprzeczenie w.w.
# #     * \b - samodzielne slowo
# https://docs.python.org/3/library/re.html#regular-expression-syntax


#
# # %%
#
# print(re.search(r'\s+', 'Warszawa        to piekne miasto'))
#
# # %%
#
# print(re.search(r'\S+', 'Warszawa to piekne miasto '))
#
# # %%
#
# print(re.search(r'\S+', 'Wars334&zawa to piekne miasto'))
#
# # %%
#
# print(re.search(r'\w+', 'Warszawa to piekne miasto'))
#
# # %%
#
# print(re.search(r'\W+', 'Warszawa++?*)%^&)234??? to piekne miasto'))
#
# # %%
#
# print(re.search(r'\d+', 'Warszawa++?*)%^&)23434??? to piekne miasto'))
# print(re.search(r'\d+?', 'Warszawa++?*)%^&)234??? to piekne miasto'))
#
# # %%
#
# print(re.search(r'\D+', 'Warszawa++?*)%^&)234576??? to piekne miasto'))
#
# # {m} oznacza ile powtórzeń danego znaku chcemy
#
# print(re.search(r'\d{2}-\d{3}', '02-081').group())
# print(re.search(r'\d{2}-\d{3}', '022-081').group())
#
# # {m,n} określa dokładny zakres ilości powtórzeń


#
# print(re.search(r'\d{3,4}-\d{3}', '0289-081'))
# # print(re.search(r'\d{4,}-\d{3}', '02289-081'))
# # #
# # A co jeśli chcemy znaleźć napisy z ukośnikami, kropkami lub plusami?
# Może posłużyć się znakiem 'ucieczki': \
#

# print(re.search(r'\d+\+\d+', '22+2'))
# print(re.search(r'\d+[+]\d+', '22+2'))
# print(re.search(r'\d+\*\d+', '2*2'))
# print(re.search(r'\d+\+\d+', '+2'))
#
# # W nawiasach kwadratowych możemy określać również zakres np od a do z:
# [a-z] oraz od 0 do 9 [0-9],
# # czyli w praktyce wszystkie litery lub cyfry
#
# print(re.search(r'[a-z]+', 'falafel'))
# print(re.search(r'[a-z*]+', 'fala**fel'))
#
# print(re.search(r'\d', '9573528'))
# print(re.search(r'[0-8]+', '9573528'))
#
# print(re.search(r'[0-9]+[a-z]+', '9573528hafdyusk94635'))
# print(re.search(r'[0-9][a-z]+', '9573528hafdyusk94635'))
#
# # %%
#
# print(re.search(r'[abc]+', 'abcccccabcabcabc'))
# print(re.search(r'[abc]+', 'abccccc_abc_abc_abc'))
# print(re.search(r'[c-d]+', 'abccccc_abc_abc_abc'))
# print(re.search(r'[c-d]+?', 'abccccc_abc_abc_abc'))
#
# # Znaki specjalne tracą swoje specjalne znaczenie w nawiasach kwadratowych
# np [(+*)] oznacza znajdź mi otwarcie okrągłego nawiasu, plus,
# gwiazdkę lub zamknięcie okrągłego nawiasu
#
# # %%
#

# print(re.search(r'[(+*)]', 'ababa + ababa'))
# print(re.search(r'[(+*)]+', 'ababa ((++ ababa '))
#
# # W nawiasach kwadratowych zastosowanie ^ oznacza znak wykluczenia,
# a więc będziemy szukać wszystkiego poza tym znakiem
#
# print(re.search(r'[^51]+jajko[^5]+', '551234jajko67589'))
#
# # %%
#
# print(re.search(r'Warszawa|Krakow', 'Krakow to piekne miasto'))
#
# # Aby znaleźć wszystkie dopasowania stosujemy findall() zamiast search()
#
# print(re.findall(r'\w+', 'Warszawa to piekne miasto 234'))
#
# # Możemy też wykorzystać wyrażenia regularne do zamiany na inny string dzięki wykorzystaniu sub()
# # %%
#

# print('ala ma kotra'.replace("kotra", "kota"))
# print(re.sub(r'\w+', 'zmieniony', 'Warszawa to piekne miasto &&??'))


#
#
# # https: // regex101.com /
#
# to jest komentarz
# todo
# # 1. Znajdźmy w poniższym stringu numery telefonów
#
# string_to_clean = 'BTgMrF0npR665-5544-63BTgMrF0npR735-5520-51BTgMrF0npR885-5543-07BTgMrF0npR795-5583-74BTgMrF0npR505-5574-48BTgMrF0npR735-5514-34BTgMrF0npR455-5578-66BTgMrF0npR575-5596-20BTgMrF0npR605-5581-78BTgMrF0npR695-5575-18BTgMrF0npR885-5525-86BTgMrF0npR455-5535-05BTgMrF0npR785-5577-67BTgMrF0npR665-5533-11BTgMrF0npR695-5594-32BTgMrF0npR535-5540-51BTgMrF0npR785-5568-32BTgMrF0npR575-5592-96BTgMrF0npR455-5563-01BTgMrF0npR605-5537-21BTgMrF0npR455-5531-45BTgMrF0npR725-5534-83BTgMrF0npR885-5542-59BTgMrF0npR795-5516-02BTgMrF0npR695-5585-66BTgMrF0npR505-5572-18BTgMrF0npR735-5590-00BTgMrF0npR505-5543-71BTgMrF0npR735-5542-93BTgMrF0npR535-5563-43BTgMrF0npR665-5518-66BTgMrF0npR665-5538-23BTgMrF0npR605-5568-72BTgMrF0npR885-5549-15BTgMrF0npR455-5566-28BTgMrF0npR785-5580-92BTgMrF0npR695-5583-90BTgMrF0npR535-5561-47BTgMrF0npR505-5586-43BTgMrF0npR455-5550-78 '

# todo
# # 2. Znajdź jedynie imiona żeńskie
#
imiona = 'Balbina, Barbara, Beata, Berenika, Bernadeta, Bianka, Blanka, Bogda, Bogna, Bogumiła, Bogusława, Edyta, ' \
 'Bartłomiej, Bartosz, Bastian, Beniamin, Benjamin, Bernard, Błażej, Bogumił, Bolesław, Borys, Bożydar, ' \
 'Brajan, Eftalia, Elena, Eleonora, Eliza, Elwira, Jadwiga, Jagna, Jagoda, Jana, Janina, Jaśmina, Leokadia, ' \
 'Jessica, Joanna, Jola, Jacek, Jacob, Jakub, Jan, Janusz, Jarosław, Jeremi, Jeremiasz, Jerzy, Jędrzej, Joachim'
#



# NIEZALEŻNE SLOWA
# print(re.findall(r' ma ', 'mama ma kota i maluje.ma kota'))
# print(re.findall(r' ma', 'ona to ma.'))
# print(re.findall(r'ma ', 'ma ona to'))
# # to co ponizej == powyzej:
# print(re.findall(r'\bma\b', 'mama ma kota i maluje.ma kota'))
# print(re.findall(r'\bma\b', 'ona to ma.'))
# print(re.findall(r'\bma\b', 'ma ona to'))


# szukamy paternu z początkiem ale chcemy wyswietlic bez poczatku
# ?<=
# ?<!
# print(re.search('(?<=abc)def', 'abcdef').group())
# ==
# print(re.search('abcdef', 'abcdef').group()[3:])
# print(re.findall('(?<!\d)[a-z]+', 'abcdef 567abc'))

# print(re.search('DEF', 'abcdef', flags=re.IGNORECASE).group())


# todo
# # 3. Stwórz słownik ile razy występuje jak długi ciąg liter 'i' w napisie
# #
# super_napis = 'piigiiiihiiiiiiiihihihihiffffffiiiiiiiiiiikikikikikikiloiiiiiiiiiiiiiaaaaaaappppppppppppppppyyyyyyyyyyyyhihihihihihiiiiiiii'

#
# todo
# 4. Znajdź adresy mailowe
#
# napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'
# #


# todo
# # 5. Zamień domene z adresów mailowych na onet.pl
# napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'
# #

# todo
# # 6. Napisz wyrażenie wyszukujące, czy w stringu znajduje się 'q' lub 'Q'
#
# super_string = ',kwa kwa qua'


# todo
# # 7. Napisz wyrażenie wyszukujące, czy w stringu znajduje się '*'
#
# super_string = 'moj super string z gwiazdka *'


# todo
# # 8. Stwórz słownik danych osobowych z poniższego stringa
# Przyjmijmy, że zawsze w naszym zbiorze na początku występuje imie i nazwisko
# oraz, że poniższy string reprezentuje sposob zapisu naszych danych
#
string_z_danymi = 'Karol Kowalski, ul.Prosta 5/10, 675-835-578, 04-445'

#
# todo
# # 9. Napisz wyrażenie wyszukujące, czy w stringu znajdują się
# dwie samogłoski pod rząd (a,e,i,o,u)
#
# super_string = 'moaj supear string z gwiazdka *'
# super_string_bez = 'moj supr string z gwazdka *'

#
# todo
# # 10. Napisz wyrażenie wyszukujące, czy w stringu znajduje się przynajmniej
# 6 cyfr (w sumie)
#
# dlugi_string = '* 345445 ja'
# krotki_string = '12 ja 45 on 6 ty'
#


# todo
# # 11. Napisz pętlę określającą, czy w stringu znajduje się słowo 'obiad'
#
# moja_obiadowa_lista = [
#  'ale super obiad',  # True
#  'tu nie maobiad',  # False
#  'chce do domu',  # False
#  'zima idzie',  # False
#  'bedzie obiad?',  # True
#  'obiad     '  # True
# ]
