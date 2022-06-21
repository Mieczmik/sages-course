# ZADANIE 2: w podanym napisie wyświetl wszystkie słowa
# na literę "a":
napis = 'ala ma kota a anna psa'

words = [elem for elem in napis.split(' ') if elem[0].lower() == 'a']
print(words)




