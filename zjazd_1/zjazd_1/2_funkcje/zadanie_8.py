# ZADANIE 8: Napisz 2_funkcje, zamieniającą literę a
#  w napisie na "X". ‘Ala’ -> XlX
inputStr = "Ala"

def outputStr(inputStr):
    inputStr = inputStr.replace('a', 'X')
    inputStr = inputStr.replace('A', 'X')
    return print(inputStr)

outputStr(inputStr)