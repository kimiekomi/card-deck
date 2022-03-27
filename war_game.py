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

        self.cards_on_table = []
            
        self.player_battle = self.player_deck.get_card()
        self.cards_on_table.append(self.player_battle)
        self.player_battle.reveal_card()
        
        self.rival_battle = self.rival_deck.get_card()
        self.cards_on_table.append(self.rival_battle)
        self.rival_battle.reveal_card()

        if self.player_battle.equal_value(self.rival_battle):
            self.lets_war()

        else:
            if trace: print(f"value compare: {self.player_card.greater_value(self.rival_card)}")

            self.clear_table(player_battle, rival_battle)
            
        cards_on_table = []

        
    def lets_war(self):
        if debug: print("initialized lets_war()")

        while True:
            for i in range(2):
                self.cards_on_table.append(self.player_deck.get_card())
                
            self.player_war4 = self.player_deck.get_card()
            self.cards_on_table.append(self.player_war4)
            self.player_war4.reveal_card()
    
            if trace: print(f"player war-cards: {self.player_war1}, {self.player_war2}, {self.player_war3}, {self.player_war4}")
            if trace: print(f"\nrival war-cards: {self.rival_war1}, {self.rival_war2}, {self.rival_war3}, {self.rival_war4}")
    
            for i in range(2):
                self.cards_on_table.append(self.rival_deck.get_card())
                
            self.rival_war4 = self.rival_deck.get_card()
            self.cards_on_table.append(self.rival_war4)
            self.rival_war4.reveal_card()
    
            if trace: print(f"cards on table: {self.cards_on_table}")
    
            if self.player_war4.equal_value(self.rival_war4):
                continue

            self.clear_table(self.player_war4, self.rival_war4)
            
        
    def clear_table(self, player_card, rival_card):
        if debug: print("initialized clear_table()")
            
        if self.player_card.greater_value(self.rival_card) == True:

            for card in self.cards_on_table:
                card.conceal_card()
                self.player_deck.insert(0, card)

            self.player_score += (len(cards_on_table) / 2)
            self.rival_score -= (len(cards_on_table) / 2)

        else:
            for card in self.cards_on_table:
                card.conceal_card()
                self.rival_deck.insert(0, card)

            self.rival_score += (len(cards_on_table) / 2)
            self.player_score -= (len(cards_on_table) / 2)

        if trace: print(f"player score: {self.player_score}, rival score: {self.rival_score}")

        
if __name__ == "__main__":
    war_game()
    
