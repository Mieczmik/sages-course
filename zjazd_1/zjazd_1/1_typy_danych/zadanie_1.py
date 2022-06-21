# ZADANIE 1: stworz zmienne: imie(str), nazwisko(str),
# ilosc zwierząt domowych(int).
# Następnie utwórz z nich napis: "nazywam się
# IMIE NAZWISKO i mam
# ILOSC zwierząt domowych. Zamień wszystkie litery
# na wielkie
# oraz wybierz elementy od 2 do 10 napisu

name = 'Mikolaj'
surname = 'Miecznikowski'
pets_numbers = 1

writing = f'Nazywam się {name} {surname} i mam {pets_numbers} zwierząt domowych.'
print(writing)
print(writing.upper())
print(writing[1:11])
