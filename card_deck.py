#! /usr/bin/env python3

import random

debug = True
trace = False

Ace = 1
Jack = 11
Queen = 12
King = 13

Spades = 1
Clubs = 2
Hearts = 3
Diamonds = 4

class Card():

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit


    def __repr__(self):
    
        if self.suit == Spades:
            suit = "Spades"

        elif self.suit == Clubs:
            suit = "Clubs"

        elif self.suit == Hearts:
            suit = "Hearts"

        elif self.suit == Diamonds:
            suit = "Diamonds"
            
            
        if self.rank == Ace:
            rank = "Ace"

        elif self.rank == Jack:
            rank = "Jack"

        elif self.rank == Queen:
            rank = "Queen"

        elif self.rank == King:
            rank = "King" 

        else:
            rank = str(self.rank)
            
        return f"'{self.rank}' of '{self.suit}'"


    def print(self):
        print(self.__repr__())


class Deck():

    def __init__(self):
        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        
        self.deck = []

        for suit in suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in ranks:
                if trace: print(f"looping through rank: '{rank}'")
                
                card = Card(suit, rank)
                self.deck.append(card)


    def shuffle(self):
        random.shuffle(self.deck)


    def deal_a_card(self):
        return self.deck.pop()

    
    def reveal(self, dealt_card):
        dealt_card.display()


    def isEmpty(self):
        return True

    
    def print(self):
        
        for card in self.deck:
            print(card)
        
if __name__ == "__main__":
    ace_of_spades = Card("Spades", "Ace")
    two_of_clubs = Card("Clubs", 2)
    jack_of_diamonds = Card("Diamonds", "Jack")
    queen_of_hearts = Card("Hearts", "Queen")
    king_of_diamonds = Card("Diamonds", "King")

    ace_of_spades.print()
    two_of_clubs.print()
    jack_of_diamonds.print()
    queen_of_hearts.print()
    print(king_of_diamonds)

    
    # deck = Deck()

    # deck.print ()

    # deck.shuffle()

    # deck.print()

    # while not deck.isEmpty():
    #     print (deck.deal_a_card())

