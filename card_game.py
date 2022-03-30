#! /usr/bin/env python3

from card_class import *
from deck_class import *

class CardGame:

    def __init__(self):

        self.deck = Deck(self, shuffled=True)


if __name__ == "__main__":
    game = CardGame()

