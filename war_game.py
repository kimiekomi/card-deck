#! /usr/bin/env python3

from card_class import *
from deck_class import *

debug = True
trace = True

class WarGame():
    def __init__(self):
        self.player_score = 26
        self.rival_score = 26

        deck = Deck()

        self.player_deck = []
        for i in range(self.player_score):
            self.player_deck.append(deck.get_card())

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}")

        self.rival_deck = []
        for i in range(self.rival_score):
            self.rival_deck.append(deck.get_card())

        if trace: print(f"\nrival deck({len(self.rival_deck)}): {self.rival_deck}")


if __name__ == "__main__":
    war_game()
    
