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

class Card:

    def __init__(self, suit, rank, game=None):

        self.suit = suit
        self.rank = rank
        self.value = rank

        if self.value == Ace:
            self.value += 13
            
        self.game = game
        self.face_up = True
        

    def reveal_card(self):
        self.face_up = True
        return self.face


    def conceal_card(self):
        self.face_up = False
        return self.face


    def is_face_card(self):
        return self.rank == Jack or self.rank == Queen or self.rank == King

    
    def __lt__(self, other):

        if self.game != None:
            return self.game.card_less_than(self, other)
            
        return self.value < other.value
        

    def __eq__(self, other):
        if self.game != None:
            return self.game.card_equal_to(self, other)

        return self.value == other.value


    def __gt__(self, other):
        if self.game != None:
            return self.game.card_greater_than(self, other)

        return self.value > other.value

        
    def same_suit(self, other):
        return self.suit == other.suit 
        

    def __repr__(self):

        if self.face_up == False:
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
    
    print(jack_of_diamonds > two_of_spades)
    print(queen_of_hearts == two_of_spades)
    print(ace_of_spades < two_of_spades)

    # print(two_of_clubs.is_face_card())
    # print(queen_of_hearts.is_face_card())
    # print(ace_of_spades.is_face_card())

