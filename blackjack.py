#! /usr/bin/env python3

from playing_card import *
from card_deck import *
from card_game import *

debug = True
trace = False

class BlackJack(CardGame):

    def __init__(self, initial_bet=10):
        super().__init__()

        self.initial_bet = initial_bet
        self.player_bank = -(self.initial_bet)
        self.dealer_bank = self.initial_bet

        # burn card
        self.deck.get_card()

        if trace: print(f"\ngame deck({len(self.deck)}): {self.deck}")

        self.player_hand = []
        self.dealer_hand = []

        for i in range(2):
            if len(self.deck) > 0:
                self.player_hand.append(self.deck.get_card())
                self.dealer_hand.append(self.deck.get_card())

        print(f"\nplayer hand({len(self.player_hand)}): {self.player_hand}\ndealer hand({len(self.player_hand)}): [{self.dealer_hand[0]}, _ of _]")


    def play(self):
        if debug: print(f"\ncalled play() with initial bet: ${self.initial_bet}")

        self.player_hand_total = 0
        for card in self.player_hand:
            self.player_hand_total += card.value
            
        self.dealer_hand_total = 0
        for card in self.dealer_hand:
            self.dealer_hand_total += card.value

        print(f"player hand total: {self.player_hand_total}") 
        if trace: print(f"dealer hand total: '{self.dealer_hand_total}'")
        print(f"dealer card1 value: {self.dealer_hand[0].value}") 

        player_options = input("\nEnter next move: ").lower()
        
        if player_options[0] == "h":
            self.hit()

        elif player_options[0] == "s":
            self.split()

        elif player_options[0] == "d":
            self.double()

        else:
            if self.player_hand_total == 21 and self.dealer_hand_total != 21:
                print("Player has Blackjack")
                self.player_bank += (1.5 * self.initial_bet)
    
            if self.dealer_hand_total == 21 and self.playerer_hand_total != 21:
                print("Dealer has Blackjack")
    
            if self.player_hand_total == 21 and self.dealer_hand_total == 21:
                print("Both have Blackjack")
                self.player_bank += self.initial_bet

        if trace: print(f"\nplayer bank: ${self.player_bank}\ndealer bank: ${self.dealer_bank}")


    def hit(self):
        pass


    def split(self):
        pass


    def double(self):
        pass


    def insurance(self):
        pass

if __name__ == "__main__":
    game = BlackJack()
    game.play()
    
