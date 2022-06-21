# ZADANIE 9: Napisz 2_funkcje, zamieniającą pierwszą
# literę a w napisie na "X".
# Ala -> Xla

#print('ala ma kota kota'.find('kota'))

moj_napis = 'LAla'

#print(moj_napis.lower().index('l'))

def change(s):
    newstring = 'X'
    index = moj_napis.lower().index('l')
    s = s[:index] + newstring + s[index + 1:]
    return print(s)

change(moj_napis)