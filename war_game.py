#! /usr/bin/env python3

from card_class import *
from deck_class import *

debug = True
trace = True

class WarGame():
    def __init__(self):
        self.player_score = 26
        self.computer_score = 26

        deck = Deck()
        deck.shuffle()

        self.player_deck = []
        for i in range(self.player_score):
            self.player_deck.append(deck.get_card())

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}")

        self.computer_deck = []
        for i in range(self.computer_score):
            self.computer_deck.append(deck.get_card())

        if trace: print(f"\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")


    def lets_battle(self):
        if debug: print("initialized lets_battle()")

        while True:
            self.cards_on_table = []
                
            self.player_battle_card = self.player_deck.pop()
            self.cards_on_table.append(self.player_battle_card)
            self.player_battle_card.reveal_card()
            
            self.computer_battle_card = self.computer_deck.pop()
            self.cards_on_table.append(self.computer_battle_card)
            self.computer_battle_card.reveal_card()
    
            if self.player_battle_card.equal_value(self.computer_battle_card):
                if trace: print("cards have equal value...time to war")
                self.lets_war()
    
            else:
                if trace: print(f"cards have different values")
    
                self.clear_table(self.player_battle_card, self.computer_battle_card)
            
            self.cards_on_table = []

            if trace: print(f"cards on table: {self.cards_on_table}")

            if self.player_score == 0:
                print("Game Over...Computer Won")

            elif self.computer_score == 0:
                print("Game Over...Player Won")
                
            else:
                response = input("Reveal another card? ")
        
                if response[0].lower == "y":
                    continue
                    
                else:    
                    print("\nYou lost the war by forfeiture")
                    break
                
        
    def lets_war(self):
        if debug: print("initialized lets_war()")

        while True:
            for i in range(2):
                self.cards_on_table.append(self.player_deck.pop())
                
            self.player_war_card = self.player_deck.pop()
            self.cards_on_table.append(self.player_war_card)
            self.player_war_card.reveal_card()
    
            for i in range(2):
                self.cards_on_table.append(self.computer_deck.pop())
                
            self.computer_war_card = self.computer_deck.pop()
            self.cards_on_table.append(self.computer_war_card)
            self.computer_war_card.reveal_card()

            if trace: print(f"cards on table: {len(self.cards_on_table)}")
    
            if self.player_war_card.equal_value(self.computer_war_card):
                if trace: print("cards have equal value...time to war")
                continue

            self.clear_table(self.player_war_card, self.computer_war_card)
            
        
    def clear_table(self, player_card, computer_card):
        if debug: print("initialized clear_table()")

        if trace: print(f"player card: {player_card} \ncomputer card: {computer_card}")

        if player_card.greater_value(computer_card) == True:
            if trace: print("player card is higher")

            for card in self.cards_on_table:
                card.conceal_card()
                self.player_deck.insert(0, card)

            self.player_score += (len(self.cards_on_table) / 2)
            self.computer_score -= (len(self.cards_on_table) / 2)

        else:
            if trace: print("computer card is higher")
            
            for card in self.cards_on_table:
                card.conceal_card()
                self.computer_deck.insert(0, card)

            self.computer_score += (len(self.cards_on_table) / 2)
            self.player_score -= (len(self.cards_on_table) / 2)

        if trace: print(f"cards on table: {len(self.cards_on_table)}")

        if trace: print(f"player score: {self.player_score}, computer score: {self.computer_score}")

        
if __name__ == "__main__":
    war_game = WarGame()
    war_game.lets_battle()
    
