#! /usr/bin/env python3

import random

debug = True
trace = False

Ace = 14
Jack = 11
Queen = 12
King = 13

Spades = 1
Clubs = 2
Hearts = 3
Diamonds = 4

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank
        self.face = True


    def reveal_card(self):
        self.face = True
        return self.face


    def conceal_card(self):
        self.face = False
        return self.face


    def __lt__(self):
        pass


    def __eq__(self):
        pass


    def __gt__(self):
        pass

        
    def same_suit(self, card):
        return self.suit == card.suit 
        

    def compare_value(self, card):
        return self.value - card.value


    def greater_value(self, card):
        return self.value > card.value


    def equal_value(self, card):
        return self.value == card.value


    def lesser_value(self, card):
        return self.value < card.value

    
    def __repr__(self):

        if self.face == 0:
            return f"_ of _, value: _"
             
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
        
        return f"{rank} of {suit}"


    def print(self):
        print(self.__repr__())


if __name__ == "__main__":
    ace_of_spades = Card(Spades, Ace)
    two_of_clubs = Card(Clubs, 2)
    two_of_spades = Card(Spades, 2)
    jack_of_diamonds = Card(Diamonds, Jack)
    queen_of_hearts = Card(Hearts, Queen)
    king_of_diamonds = Card(Diamonds, King)

    # ace_of_spades.print()
    # two_of_clubs.print()
    # two_of_spades.print()
    # jack_of_diamonds.print()
    # queen_of_hearts.print()
    # print(king_of_diamonds)

    # ace_of_spades.reveal_card()
    # ace_of_spades.print()
    # ace_of_spades.conceal_card()
    # ace_of_spades.print()

    # print(ace_of_spades.same_suit(two_of_spades))
    # print(ace_of_spades.same_suit(two_of_clubs))
    
    # print(two_of_clubs.compare_rank(two_of_spades))
    # print(two_of_clubs.compare_rank(ace_of_spades))
    
    # print(two_of_clubs.compare_value(two_of_spades))
    # print(jack_of_diamonds.compare_value(two_of_spades))

    # print(jack_of_diamonds.greater_rank(two_of_spades))
    # print(queen_of_hearts.equal_rank(two_of_spades))
    # print(ace_of_spades.lesser_rank(two_of_spades))

    # print(jack_of_diamonds.greater_rank(two_of_spades))
    # print(queen_of_hearts.equal_rank(two_of_spades))
    # print(ace_of_spades.lesser_rank(two_of_spades))

