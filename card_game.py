#! /usr/bin/env python3

from card_class import *
from deck_class import *

class CardGame:

    def __init__(self):
        self.deck = Deck(self, shuffled=True)


class Player:
    def __init__(self, hand):
        self.hand = hand
        self.purse = ""
        self.wager = ""


    def hit(self):
        pass


class Human(Player):
    def __init__(self, hand):
        super().__init__(hand)



class Computer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        

    
if __name__ == "__main__":
    game = CardGame()

