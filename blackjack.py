#! /usr/bin/env python3

from card_class import *
from deck_class import *
from card_game import *

debug = False
trace = False

class BlackJack(CardGame):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    game = BlackJack()

