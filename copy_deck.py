#! /usr/bin/env python3

import random

debug = True
trace = False

class Card():

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value


    def compare_suit(self, card1, card2):
        return card1.self.suit() == card2.self.suit() 
        

    def compare_rank(self, card1, card2):
        return card1.self.rank() == card2.self.rank() 


    def compare_value(self, card1, card2):
        return card1.self.value() == card2.self.value() 

    
    def __repr__(self):
        return f"'{self.rank}' of '{self.suit}', value: '{self.value}'"


    def print(self):
        print(self.__repr__())


class Deck():

    def __init__(self):
        self.ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

        self.reset()
                

    def reset(self):
        for rank in self.ranks:
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
        
        for suit in self.suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in self.ranks:
                if trace: print(f"looping through rank: '{rank}'")

                card = Card(suit, rank, value)
                self.deck.append(card)

        return self.deck
        
        
    def shuffle(self):
        random.shuffle(self.reset())


    def get_card(self):
        return self.deck.pop()


    def is_empty(self):
        if len(self.deck) == 0: return True 

    
    def print(self):
        
        for card in self.deck:
            print(card)


class WarGame():
    pass
            
        
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

    deck.reset()
    # deck.print()

    print (deck.get_card())

