#! /usr/bin/env python3

from card_class import *
from deck_class import *

debug = True
trace = True

class WarGame():

    def __init__(self):
        self.player_score = 6
        self.computer_score = 6

        deck = Deck()
        deck.shuffle()

        self.player_deck = []
        self.computer_deck = []

        for i in range(self.player_score):
            self.player_deck.insert(0, deck.get_card())
            self.computer_deck.insert(0, deck.get_card())

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}")
        
        if trace: print(f"\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")


    def play(self):

        while True:
            if debug: print("\ninitialized play()")
            
            self.cards_on_table = []

            if len(self.player_deck) == 0:
                print("Deck is empty")
                print("\n>>> Game Over...Computer Won War\n")
                break
                
            self.player_battle_card = self.player_deck.pop(0)
            self.cards_on_table.append(self.player_battle_card)
            self.player_battle_card.reveal_card()

            if len(self.computer_deck) == 0:
                print("Deck is empty")
                print("\n>>> Game Over...Player Won War\n")
                break
            
            self.computer_battle_card = self.computer_deck.pop(0)
            self.cards_on_table.append(self.computer_battle_card)
            self.computer_battle_card.reveal_card()

            print(f"player card: {self.player_battle_card} \ncomputer card: {self.computer_battle_card}")

            if self.player_battle_card.equal_value(self.computer_battle_card):
                if trace: print("cards have equal value...time for war")
                    
                self.lets_war()
    
            else:
                if trace: print("cards have different values")
    
                self.clear_table(self.player_battle_card, self.computer_battle_card)
            
            if self.player_score <= 0:
                print("\n>>> Game Over...Computer Won War\n")
                break

            if self.computer_score <= 0:
                print("\n>>> Game Over...Player Won War\n")
                break

        
    def lets_war(self):

        if debug: print("initialized lets_war()")

        while True:
        
            for i in range(3):
                if len(self.player_deck) == 0:
                    break

                self.cards_on_table.append(self.player_deck.pop())

                if len(self.computer_deck) == 0:
                    break
                    
                self.cards_on_table.append(self.computer_deck.pop())
            
            if len(self.player_deck) == 0:
                break
                
            player_war_card = self.player_deck.pop()
            self.cards_on_table.append(player_war_card)
            player_war_card.reveal_card()

            if len(self.computer_deck) == 0:
                break
                
            computer_war_card = self.computer_deck.pop()
            self.cards_on_table.append(computer_war_card)
            computer_war_card.reveal_card()

            print(f"player card: {self.player_war_card} \ncomputer card: {self.computer_war_card}")
            
            if trace: print(f"cards on table: {len(self.cards_on_table)}")
    
            if player_war_card.equal_value(computer_war_card):
                if trace: print("cards have equal value...time for war")
                continue

            self.clear_table(player_war_card, computer_war_card)
            
        
    def clear_table(self, player_card, computer_card):

        if debug: print("initialized clear_table()")

        if player_card.greater_value(computer_card) == True:
            print("player card is higher")

            for card in self.cards_on_table:
                card.conceal_card()
                self.player_deck.insert(0, card)

            self.player_score += (len(self.cards_on_table) / 2)
            self.computer_score -= (len(self.cards_on_table) / 2)

        else:
            print("computer card is higher")
            
            for card in self.cards_on_table:
                card.conceal_card()
                self.computer_deck.insert(0, card)

            self.computer_score += (len(self.cards_on_table) / 2)
            self.player_score -= (len(self.cards_on_table) / 2)

        if trace: print(f"cards on table: {len(self.cards_on_table)}")

        print(f"player score: {self.player_score}, computer score: {self.computer_score}")

        self.cards_on_table = []
        
        if trace: print(f"cards on table: {len(self.cards_on_table)}")
                

if __name__ == "__main__":
    war_game = WarGame()
    war_game.play()

