#! /usr/bin/env python3

from card_class import *
import random

debug = True
trace = False

class Deck():

    def __init__(self):

        self.ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
        self.suits = [Spades, Clubs, Hearts, Diamonds]
        self.face_up = False

        self.create_deck()


    def create_deck(self):
          
        self.deck = []
        
        for suit in self.suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in self.ranks:
                if trace: print(f"looping through rank: '{rank}'")

                if rank == Ace:
                    value = 14
                
                elif rank == Jack:
                    value = 11
                    
                elif rank == Queen:
                    value = 12
                    
                elif rank == King:
                    value = 13

                else:
                    value = int(rank)

                card = Card(suit, rank, value, 0)
                self.deck.append(card)

        return self.deck
        
        
    def shuffle(self):
        random.shuffle(self.create_deck())


    def get_card(self):
        if len(self.deck) == 0:
            return "Deck is empty"
            
        return self.deck.pop()


    def is_empty(self):
        if len(self.deck) == 0: return True 

    
    def __len__(self):
        return len(self.deck)
    
    
    def print(self):
        
        for card in self.deck:
            print(card)


if __name__ == "__main__":
    deck = Deck()
    deck.print ()

    # deck.shuffle()
    # deck.print()

    # deck.create_deck()
    # deck.print()

    # print(deck.get_card())
    # deck.print()
        
