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
        
        self.player_hand_total = None
        self.dealer_hand_total = None


    def play(self):
        if debug: print(f"\ncalled play()")

        while True:
            self.player.hand = []
            self.dealer.hand = []

            self.player_hand_total = 0
            self.dealer_hand_total = 0

            if trace: print(f"player hand({len(self.player.hand)}), dealer hand({len(self.dealer.hand)})\nplayer total: {self.player_hand_total}, dealer total: {self.dealer_hand_total}")
                
            print(f"\nPlayer Bank: ${self.player_bank}\n")
            
            try:
                self.initial_bet = int(input("Enter initial bet: $ ") or 10)

            except ValueError:
                print("> Error: Enter a valid number\n")
                continue

            self.player_bank -= self.initial_bet

            print(f"Updated Player Bank: ${self.player_bank}")

            for i in range(2):
                if len(self.deck) > 0:
                    self.player.hit()
                    self.dealer.hit()

            print(f"\ncards dealt\nplayer hand: {self.player.hand}\ndealer hand: [ _ of _, {self.dealer.hand[1]}]")

            self.player_hand_total = 0
            for card in self.player.hand:
                self.player_hand_total += card.value
                
            self.dealer_hand_total = 0
            for card in self.dealer.hand:
                self.dealer_hand_total += card.value
    
            print(f"player hand total: {self.player_hand_total}") 
            if trace: print(f"dealer hand total: {self.dealer_hand_total}")
            print(f"dealer card2 value: {self.dealer.hand[1].value}") 

            self.player_options()
            
            print(f">>> Updated Player Bank: ${self.player_bank}")
    
            another_round = input("\nAnother Round? ").lower()
    
            if another_round[0] != "y":
                print("\n>>> Goodbye...\n")
                break

            os.system("clear")


    def player_options(self):
        if debug: print("called player_options()")

        while True:
            first_option = input("\nEnter first move: ").lower()
        
            if first_option == "t":
                if trace: print("player elected to stand")
                    
                self.is_natural()
                break
        
            # elif first_option == "s":
            #     if trace: print("player elected to split pair")
        
            #     if self.player.hand[0].rank == self.player.hand[1].rank:
            #         self.split()
            #         break
        
            #     print("> equal rank cards...unable split")
            #     continue
        
            elif first_option == "d":
                if trace: print("player elected to double down")

                if self.player.hand[0].value + self.player.hand[0].value == 9 or self.player.hand[0].value + self.player.hand[0].value == 10 or self.player.hand[0].value + self.player.hand[0].value == 11:
                    self.double()
                    break

                print("> cards total not 9, 10, or 11...unable double")
                continue
        
            # elif first_option != "t" and first_option != "s" and first_option != "d" and first_option != "h":
            #     if trace: print("player elected to surrender")
                    
            #     self.surrender()
            #     break
        
            elif first_option == "h":
                if trace: print("player elected to hit")
                    
                self.hit_loop()
                break
                

    def hit_loop(self):
        if debug: print("called hit_loop()")
            
        while True:
            self.player.hit()

            self.player_hand_total += self.player.hit_card.value

            print(f"updated player hand: {self.player.hand}")
            print(f"updated player hand total: {self.player_hand_total}") 
            print(f"dealer card1 value: {self.dealer.hand[1].value}") 

            if self.player_hand_total >= 21: 
                self.define_winner()
                break

            next_option = input("\nEnter next move: ").lower()

            if next_option == "h":
                continue

            if trace: print("player elected to stand")

            self.dealers_move()
            self.define_winner()
            break
            
        
    # def split(self):
    #     if debug: print("called split()")

    #     split1 = []
    #     split2 = []

    #     split1.append(self.player_hand[0])
    #     split2.append(self.player_hand[1])


    def double(self):
        if debug: print("called double()")
            
        self.initial_bet += self.initial_bet
        self.player_bank -= (self.initial_bet/2)

        print(f"Updated Player Bank: ${self.player_bank}")

        self.player.hit()
        self.define_winner()


    # def insurance(self):
    #     pass


    # def surrender(self):
    #     pass


    def is_natural(self):
        
        while True: 
            if debug: print("called is_natural()")
    
            self.dealers_move()
                
            if self.player_hand_total == 21 and self.dealer_hand_total != 21:
                print("\n>>> Player has Natural...You Win")
                self.player_bank += self.initial_bet * 2.5
                break
    
            elif self.dealer_hand_total == 21 and self.player_hand_total != 21:
                print("\n>>> Dealer has Natural...You Lose")
                break
    
            elif self.player_hand_total == 21 and self.dealer_hand_total == 21:
                print("\n>>> Both have Natural...Its a Draw")
                self.player_bank += self.initial_bet
                break
    
            self.define_winner()
            break

    
    def dealers_move(self):
        if debug: print("called dealers_move()")

        print(f"dealer hand revealed: {self.dealer.hand}")
            
        while self.dealer_hand_total < 17:
            self.dealer.hit()
            self.dealer_hand_total += self.dealer.hit_card.value 

            if self.dealer.hit_card.rank == Ace and self.dealer_hand_total >= 17:
                break

        print(f"updated dealer hand: {self.dealer.hand}")
        print(f"updated dealer hand total: {self.dealer_hand_total}")

        
    def define_winner(self):
        
        while True:
            if debug: print("called define_winner()")
    
            if self.player_hand_total > 21:
                print("\n>>> Player Bust...You Lose")
                break
    
            if self.dealer_hand_total > 21:
                print("\n>>> Dealer Bust...You Win")
                self.player_bank += self.initial_bet * 2
                break
                
            if self.player_hand_total == 21 and self.dealer_hand_total != 21:
                print("\n>>> Player has Blackjack...You Win")
                self.player_bank += self.initial_bet * 2
                break
    
            if self.dealer_hand_total == 21 and self.player_hand_total != 21:
                print("\n>>> Dealer has Blackjack...You Lose")
                break
                
            if self.player_hand_total == 21 and self.dealer_hand_total == 21:
                print("\n>>> Both have Blackjack")
                self.player_bank += self.initial_bet
                break
                
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

                break

                
if __name__ == "__main__":
    game = BlackJack()
    game.play()
    

# if dealer's face-up card is ace...ask if player wants insurance??

