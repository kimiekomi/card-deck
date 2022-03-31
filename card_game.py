#! /usr/bin/env python3

from playing_card import *
from card_deck import *
import random

debug = False
trace = False

class CardGame:

    def __init__(self):
        self.deck = Deck(self, shuffled=True)
        self.remove_card = False

        if trace: print(f"shuffled_deck({len(self.deck)}): {self.deck}")


class Player:
    def __init__(self):
        self.hand = []
        self.hand_total = 0
        # self.purse = ""
        # self.wager = ""


    def __repr__(self):
        return str(self.hand)

    
    def hit(self):
        pass


class Human(Player):
    def __init__(self):
        super().__init__()


class Computer(Player):
    def __init__(self):
        super().__init__()
        

    
if __name__ == "__main__":
    game = CardGame()
    
    player = Player()
    print(player)

    human = Human()
    print(player)

    computer = Computer()
    print(player)
    