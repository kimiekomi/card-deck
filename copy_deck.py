#! /usr/bin/env python3

import random

debug = True
trace = False

class Card():

    def __init__(self, suit, rank, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        

    def __repr__(self):
        return f"'{self.rank}' of '{self.suit}', value: '{self.value}'"


    def print(self):
        print(self.__repr__())


class Deck():

    def __init__(self):
        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

        for rank in ranks:
            if rank == "Ace":
                value = 1
    
            elif rank == "Jack":
                value = 11
    
            elif rank == "Queen":
                value = 12
    
            elif rank == "King":
                value = 13
    
            else:
                value = rank
        
        self.deck = []

        for suit in suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in ranks:
                if trace: print(f"looping through rank: '{rank}'")
                
                card = Card(suit, rank, value)
                self.deck.append(card)


    def shuffle(self):
        random.shuffle(self.deck)


    def deal_a_card(self):
        return self.deck.pop()

    
    def isEmpty(self):
        return True 

    
    def print(self):
        
        for card in self.deck:
            print(card)
        
if __name__ == "__main__":
    # ace_of_spades = Card("Spades", "Ace", 1)
    # two_of_clubs = Card("Clubs", 2, 2)
    # jack_of_diamonds = Card("Diamonds", "Jack", 11)
    # queen_of_hearts = Card("Hearts", "Queen", 12)
    # king_of_diamonds = Card("Diamonds", "King", 13)

    # ace_of_spades.print()
    # two_of_clubs.print()
    # jack_of_diamonds.print()
    # queen_of_hearts.print()
    # print(king_of_diamonds)

    
    deck = Deck()

    # deck.print ()

    deck.shuffle()

    # deck.print()

    while not deck.isEmpty():
        print (deck.deal_a_card())

