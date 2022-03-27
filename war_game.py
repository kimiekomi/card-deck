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
        deck.shuffle()

        self.player_deck = []
        for i in range(self.player_score):
            self.player_deck.append(deck.get_card())

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}")

        self.rival_deck = []
        for i in range(self.rival_score):
            self.rival_deck.append(deck.get_card())

        if trace: print(f"\nrival deck({len(self.rival_deck)}): {self.rival_deck}")


    def lets_battle(self):
        if debug: print("initialized lets_battle()")
            
        self.player_card = self.player_deck.get_card()
        self.player_card.reveal_card()
        
        self.rival_card = self.rival_deck.get_card()
        self.rival_card.reveal_card()

        if self.player_card.greater_value(self.rival_card) == True:
            if trace: print(f"value compare: {self.player_card.greater_value(self.rival_card)}")

            self.player_deck

        
        

        
    # Elements: card face up/down, add card to bottom of deck, clear table


if __name__ == "__main__":
    war_game()
    
