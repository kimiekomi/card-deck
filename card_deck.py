#! /usr/bin/env python3

debug = True
trace = True

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck():

    def __init__(self):
        pass


    def shuffle(self):
        pass


    def deal(self):
        pass


def display_cards():
    if debug: print("initialized display_cards()")
    
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = [1, 2, 3, 4]

    cards = []

    for rank in ranks:
        if trace: print(f"looping through rank: '{rank}'")

        for suit in suits:
            if trace: print(f"looping through suit: '{suit}'")
            cards.append([rank, suit])

    return cards
    

    
if __name__ == "__main__":
    print(display_cards())

