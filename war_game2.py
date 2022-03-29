#! /usr/bin/env python3

from card_class import *
from deck_class import *

debug = True
trace = True

testing = True

class WarGame():

    def __init__(self):

        deck = Deck()

        if testing:
            for i in range(38):
                deck.get_card()

        deck.shuffle()

        self.player_deck = []
        self.computer_deck = []
        self.cards_on_table = []

        while deck.has_cards():
            self.player_deck.insert(0, deck.get_card())
            self.computer_deck.insert(0, deck.get_card())

        if trace: print(f"player deck({len(self.player_deck)}): {self.player_deck}")
        if trace: print(f"\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")
        if trace: print ()

    
    def play(self):
        if debug: print("play()")

        while len(self.player_deck) > 0 and len(self.computer_deck):

            # input ("\ncontinue? ")

            if len (self.cards_on_table) > 0:

                if trace: print (f"there are {len (self.cards_on_table)} cards still on the table, so we must be at war....")
            
            print ("player hand")

            for card in self.player_deck:
                print (" ", card)

            print ()

            print ("computer hand")
            
            for card in self.computer_deck:
                print (" ", card)

            print ()

            # if len(self.player_deck) == 0:
            #     print("Deck is empty")
            #     print("\n>>> Game Over...Computer Won War\n")
            #     break
                
            player_card = self.player_deck.pop()
            self.cards_on_table.append(player_card)
            player_card.reveal_card()

            # if len(self.computer_deck) == 0:
            #     print("Deck is empty")
            #     print("\n>>> Game Over...Player Won War\n")
            #     break
            
            computer_battle_card = self.computer_deck.pop()
            self.cards_on_table.append(computer_card)
            computer_card.reveal_card()

            print(f"player card: {player_card} \ncomputer card: {computer_card}")

            if player_card.equal_value(computer_card):
                if trace: print("cards are equal, so it's time for war")
                    
                self.lets_war()
                continue
        
            self.clear_table(self.player_battle_card, self.computer_battle_card)


        if len(self.player_deck) == 0:
            print ("you lost")

        else:
            print ("you won")


    def lets_war(self):

        if debug: print("lets_war()")
        
        for i in range(3):

            if len(self.player_deck) == 0:
                break

            self.cards_on_table.append(self.player_deck.pop())

            if len(self.computer_deck) == 0:
                break
                
            self.cards_on_table.append(self.computer_deck.pop())


    def clear_table(self, player_card, computer_card):
        if debug: print("clear_table()")

        if player_card.greater_value(computer_card):
            print("player card is higher")

            for card in self.cards_on_table:
                # card.conceal_card()
                self.player_deck.insert(0, card)

        else:
            print("computer card is higher")
            
            for card in self.cards_on_table:
                # card.conceal_card()
                self.computer_deck.insert(0, card)

        if trace: print(f"cards on table: {len(self.cards_on_table)}")

        print(f"player score: {len(self.player_deck)}, computer score: {len(self.computer_deck)}")

        self.cards_on_table = []
        
        if trace: print(f"cards on table: {len(self.cards_on_table)}")
                

if __name__ == "__main__":
    war_game = WarGame()
    war_game.play()

