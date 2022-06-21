# ZADANIE 7: napisz funkcję przyjmującą string z wielkimi
#  i małymi literami,
# zwróć nowy string, który będzie zawierał najpierw małe
# potem wielkie litery napisu.
# ‘DoM jESt’ > ‘ojtDMES’
inputStr = "DoM jESt"

def outputStr(inputStr):
    inputStr = inputStr.strip()
    return print(f'Małe litery stringa: {inputStr.lower()}. \nDuże litery stringa: {inputStr.upper()}.')

outputStr(inputStr)