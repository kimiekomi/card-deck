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

    def __init__(self, suit, rank, value, face):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.face = face


    def reveal_card(self):
        self.face = "up"
        return self.face

        
    def same_suit(self, card):
        return self.suit == card.suit 
        

    def compare_rank(self, card):
        return self.rank - card.rank 


    def compare_value(self, card):
        return self.value - card.value


    def greater_rank(self, card):
        return self.rank > card.rank


    def equal_rank(self, card):
        return self.rank == card.rank


    def lesser_rank(self, card):
        return self.rank < card.rank


    def greater_value(self, card):
        return self.value > card.value


    def equal_value(self, card):
        return self.value == card.value


    def lesser_value(self, card):
        return self.value < card.value

    
    def __repr__(self):
        if self.face == "down":
            
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
        
        return f"{rank} of {suit}, value: {self.value}"


    def print(self):
        print(self.__repr__())


if __name__ == "__main__":
    ace_of_spades = Card(Spades, Ace, 1, "down")
    # two_of_clubs = Card(Clubs, 2, 2)
    # two_of_spades = Card(Spades, 2, 2)
    # jack_of_diamonds = Card(Diamonds, Jack, 11)
    # queen_of_hearts = Card(Hearts, Queen, 12)
    # king_of_diamonds = Card(Diamonds, King, 13)

    ace_of_spades.print()
    # two_of_clubs.print()
    # two_of_spades.print()
    # jack_of_diamonds.print()
    # queen_of_hearts.print()
    # print(king_of_diamonds)

    ace_of_spades.reveal_card()
    ace_of_spades.print()

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

