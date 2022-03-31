#! /usr/bin/env python3

from playing_card import *
from card_deck import *
from card_game import *
import os

debug = True
trace = True

class BlackJack(CardGame):

    def __init__(self): 
        super().__init__()

        self.initial_bet = 0
        self.player_bank = 0

        # burn card
        self.deck.get_card()

        if trace: print(f"\ngame deck({len(self.deck)}): {self.deck}")

        # implemented Human and Computer class
        self.player = Human()
        self.dealer = Computer()
        
        self.player_hand = self.player.hand
        self.dealer_hand = self.dealer.hand

        self.player_hand_total = None
        self.dealer_hand_total = None


    def play(self):
        if debug: print(f"\ncalled play()")

        while True:
            self.player_hand =[]
            self.dealer_hand = []

            self.player_hand_total = 0
            self.dealer_hand_total = 0

            if trace: print(f"player hand({len(self.player_hand)}), dealer hand({len(self.dealer_hand)})\nplayer total: {self.player_hand_total}, dealer total: {self.dealer_hand_total}")
                
            for i in range(2):
                if len(self.deck) > 0:
                    self.player_hand.append(self.deck.get_card())
                    self.dealer_hand.append(self.deck.get_card())

            print(f"Player Bank: ${self.player_bank}\n")
            
            try:
                self.initial_bet = int(input("Enter initial bet: $ ") or 10)

            except ValueError:
                print("> Error: Enter a valid number\n")
                continue

            self.player_bank -= self.initial_bet

            print(f"Updated Player Bank: ${self.player_bank}")

            print(f"\ncards dealt\nplayer hand: {self.player_hand}\ndealer hand: [ _ of _, {self.dealer_hand[1]}]")

            self.player_hand_total = 0
            for card in self.player_hand:
                self.player_hand_total += card.value
                
            self.dealer_hand_total = 0
            for card in self.dealer_hand:
                self.dealer_hand_total += card.value
    
            print(f"player hand total: {self.player_hand_total}") 
            if trace: print(f"dealer hand total: '{self.dealer_hand_total}'")
            print(f"dealer card2 value: {self.dealer_hand[1].value}") 

            first_move = input("\nEnter first move: ").lower()

            if first_move != "h":
                if trace: print("player elected to 'stand'")
                    
                self.natural()

            else:
                while True:
                    self.hit()
        
                    if self.player_hand_total >= 21: 
                        self.define_winner()
                        break
                    
                    player_options = input("\nEnter next move: ").lower()

                    if player_options == "h":
                        continue
        
                    # elif player_options[0] == "s":
                    #     self.split()
            
                    # elif player_options[0] == "d":
                    #     self.double()

                    if trace: print("player elected to 'stand'")
    
                    self.dealers_move()
                    self.define_winner()
                    break

            print(f">>> Updated Player Bank: ${self.player_bank}")
    
            another_round = input("\nAnother Round? ").lower()
    
            if another_round[0] != "y":
                print("\nGoodbye...\n")
                break

            os.system("clear")

            
    def hit(self):
        if debug: print("called hit()")

        hit_card = self.deck.get_card()
        self.player_hand.append(hit_card)
        self.player_hand_total += hit_card.value

        if hit_card.rank == Ace and self.player_hand_total > 21:
            self.player_hand_total -= 10

        print(f"updated player hand: {self.player_hand}")
        print(f"updated player hand total: {self.player_hand_total}") 
        print(f"dealer card1 value: {self.dealer_hand[0].value}") 


    # def split(self):
    #     pass


    # def double(self):
    #     pass


    # def insurance(self):
    #     pass


    def natural(self):
        if debug: print("called natural()")

        self.dealers_move()
            
        if self.player_hand_total == 21 and self.dealer_hand_total != 21:
            print("\n>>> Player has Natural...You Win")
            self.player_bank += self.initial_bet * 2.5

        if self.dealer_hand_total == 21 and self.player_hand_total != 21:
            print("\n>>> Dealer has Natural...You Lose")

        if self.player_hand_total == 21 and self.dealer_hand_total == 21:
            print("\n>>> Both have Natural...Its a Draw")
            self.player_bank += self.initial_bet

        else:
            self.define_winner()

    
    def dealers_move(self):
        if debug: print("called dealers_move()")

        print(f"dealer hand revealed: {self.dealer_hand}")
            
        while self.dealer_hand_total < 17:
            dealer_card = self.deck.get_card()
            self.dealer_hand.append(dealer_card)
            self.dealer_hand_total += dealer_card.value 

            if dealer_card.rank == Ace and self.dealer_hand_total >= 17:
                break

        print(f"updated dealer hand: {self.dealer_hand}")
        print(f"updated dealer hand total: {self.dealer_hand_total}")

        
    def define_winner(self):
        if debug: print("called define_winner()")

        if self.player_hand_total > 21:
            print("\n>>> Player Bust...You Lose")

        if self.dealer_hand_total > 21:
            print("\n>>> Dealer Bust...You Win")
            self.player_bank += self.initial_bet * 2
            
        if self.player_hand_total == 21 and self.dealer_hand_total != 21:
            print("\n>>> Player has Blackjack...You Win")
            self.player_bank += self.initial_bet * 2

        if self.dealer_hand_total == 21 and self.player_hand_total != 21:
            print("\n>>> Dealer has Blackjack...You Lose")

        if self.player_hand_total == 21 and self.dealer_hand_total == 21:
            print("\n>>> Both have Blackjack")
            self.player_bank += self.initial_bet

        if self.player_hand_total < 21 and self.dealer_hand_total < 21:
            if self.player_hand_total > self.dealer_hand_total:
                print("\n>>> You are closer to 21...You Win")
                self.player_bank += self.initial_bet * 2
            
            elif self.player_hand_total == self.dealer_hand_total:
                print("\n>>> Equal Value...Its a Draw")
                self.player_bank += self.initial_bet

            else:
                self.player_hand_total < self.dealer_hand_total
                print("\n>>> Dealer is closer to 21...You Lose") 


if __name__ == "__main__":
    game = BlackJack()
    game.play()
    

# if dealer's face-up card is ace...ask if player wants insurance??

