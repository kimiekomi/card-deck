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


    def burn(self):
        self.remove_card = True
        return self.deck.get_card()


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
    
    burn_card = game.burn()
    print(f"burn_card: {burn_card}")

    game.cut()

    