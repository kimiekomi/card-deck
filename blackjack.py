#! /usr/bin/env python3

from playing_card import *
from card_deck import *
from card_game import *

debug = False
trace = False

class BlackJack(CardGame):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    game = BlackJack()

