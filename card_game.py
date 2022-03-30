from card_class import *
from deck_class import *

class CardGame:

    def __init__(self):

        self.deck = Deck(self, shuffled=True)
