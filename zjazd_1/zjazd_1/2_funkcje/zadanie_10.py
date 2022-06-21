# ZADANIE 10: Stwórz funkcję przyjmującą string.
# Policz ile znajduje się w nim liter,
# znaków specjalnych oraz cyfr
input_str = "P#@yn26at^&i5ve"

def f(input_str):
    counter = 0
    for letter in list(input_str):
        if not(letter.isalpha()) or letter.isdigit():
            counter = counter + 1
    return(print(counter))

f(input_str)

