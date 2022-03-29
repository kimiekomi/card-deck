#! /usr/bin/env python3

from card_class import *
from deck_class import *

debug = True
trace = True

class WarGame():

    def __init__(self):
        
        deck = Deck()
        deck.shuffle()

        game_deck = []
        
        for i in range(16):
            game_deck.append(deck.get_card())

        if trace: print(f"game deck({len(game_deck)}): {game_deck}")

        self.player_deck = []
        self.computer_deck = []
        self.cards_on_table = []

        while len(game_deck) > 0:
            self.player_deck.insert(0, game_deck.pop())
            self.computer_deck.insert(0, game_deck.pop())

        if trace: print(f"\nplayer deck({len(self.player_deck)}): {self.player_deck}")
        
        if trace: print(f"\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")


    def play(self):

        while len(self.player_deck) != 0 and len(self.computer_deck) != 0:
            if debug: print("\nplay()")
            
            player_battle_card = self.player_deck.pop()
            self.cards_on_table.append(player_battle_card)

            computer_battle_card = self.computer_deck.pop()
            self.cards_on_table.append(computer_battle_card)

            print(f"player card: {player_battle_card}\ncomputer card: {computer_battle_card}")

            if player_battle_card.equal_value(computer_battle_card):
                if trace: print("*cards have equal value...time for war*")
                    
                self.lets_war()
                continue
    
            else:
                if trace: print("*cards have different values*")
    
                self.clear_table(player_battle_card, computer_battle_card)
                continue
            
        if len(self.player_deck) == 0:
            print("Player Deck Empty")
            print("\n>>> Game Over...Computer Won War")

        else:
            print("Computer Deck Empty")
            print("\n>>> Game Over...Player Won War")

            # response = input("\nReveal another card? ")

            # if response[0].lower() != "y":
            #     print("\n>>> Game Over...You Surrendered")
            #     break
    
        
    def lets_war(self):

        if debug: print("lets_war()")

        for i in range(3):
            
            while len(self.player_deck) != 0 and len(self.computer_deck) != 0:
                self.cards_on_table.append(self.player_deck.pop())
                self.cards_on_table.append(self.computer_deck.pop())

        if trace: print(f"cards on table({len(self.cards_on_table)}): {self.cards_on_table}")

        return
            
            # if len(self.player_deck) == 0 or len(self.computer_deck) == 0:
            #     break
                
            # player_war_card = self.player_deck.pop()
            # self.cards_on_table.append(player_war_card)

            # computer_war_card = self.computer_deck.pop()
            # self.cards_on_table.append(computer_war_card)

            # if trace: print(f"cards on table: {len(self.cards_on_table)}")
    
            # if player_war_card.equal_value(computer_war_card):
            #     if trace: print("cards have equal value...time for war")
            #     continue

            # self.clear_table(player_war_card, computer_war_card)
            
        
    def clear_table(self, player_card, computer_card):

        if debug: print("clear_table()")

        if player_card.greater_value(computer_card) == True:
            print("<player card is higher>")

            for card in self.cards_on_table:
                self.player_deck.insert(0, card)

        else:
            print("<computer card is higher>")
            
            for card in self.cards_on_table:
                self.computer_deck.insert(0, card)

        if trace: print(f"cards on table({len(self.cards_on_table)}): {self.cards_on_table}")

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")

        print(f"player score: {len(self.player_deck)}, computer score: {len(self.computer_deck)}")

        self.cards_on_table = []
        
        if trace: print(f"table cleared: {len(self.cards_on_table)} cards on table")
                

if __name__ == "__main__":
    war_game = WarGame()
    war_game.play()

