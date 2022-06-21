# bieda-poker: Talia kart zawiera karty w kolorach: pik, kier, karo, trefl
# w zakresie od 1 do 14. Napisz funkcje, która przyjmie liczbe graczy,
# potasuje talie kart, odrzuci tyle, aby każdy gracz mial po równo
# a nastepnie rozda karty (kazdy gracz dostaje co n-tą karte).
# Nastepnie policz, który gracz / gracze otrzymał największą liczbe kart
# tego samego koloru.
import random
import itertools
from collections import Counter


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def valwithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return max(v)

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def max_number_of_the_same_color_cards(players_number):

    colors = ['hearts', 'diamonds', 'clubs', 'spades']
    numbers = list(range(1,15))

    deck = list(itertools.product(colors, numbers))
    cards_number_pp = len(deck) // players_number

    cards_to_play = random.sample(deck, cards_number_pp*players_number)

    players_name = [f'Player {i+1}' for i in range(players_number)]
    players_name

    player_cards = []
    for i in range(players_number):
        player_cards.append(cards_to_play[i::players_number])

    #Colors of card
    color_cards = []
    for elem in player_cards:
        color_cards_nested = []
        for nested_elem in elem:
            color_cards_nested.append(nested_elem[0])
        color_cards.append(list(color_cards_nested))

    zip_iterator = zip(players_name, color_cards)
    dictionary = dict(zip_iterator)


    for key in dictionary:
        dictionary[key] = dict(Counter(dictionary[key]))
        dictionary[key] = valwithmaxval(dictionary[key])

    same_color_max_cards_number = valwithmaxval(dictionary)
    players = getKeysByValue(dictionary, same_color_max_cards_number)


    return print(f' Największą liczbę kart rowną {same_color_max_cards_number} otrzymal/i {players}')

max_number_of_the_same_color_cards(6)