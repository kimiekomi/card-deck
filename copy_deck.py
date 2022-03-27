#! /usr/bin/env python3

from card_class import *
import random

debug = True
trace = False

class Deck():

    def __init__(self):

        self.ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
        self.suits = [Spades, Clubs, Hearts, Diamonds]

        self.reset()
                

    def reset(self):
          
        self.deck = []
        
        for suit in self.suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in self.ranks:
                if trace: print(f"looping through rank: '{rank}'")

                if rank == Ace:
                    value = 1
                
                elif rank == Jack:
                    value = 11
                    
                elif rank == Queen:
                    value = 12
                    
                elif rank == King:
                    value = 13

                else:
                    value = int(rank)

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


if __name__ == "__main__":
    deck = Deck()
    deck.print ()

    # deck.shuffle()
    # deck.print()

    # deck.reset()
    # deck.print()

    # print(deck.get_card())
    # deck.print()
        
