#! /usr/bin/env python3

from card_class import *
import random

debug = True
trace = False

class Deck:

    def __init__(self, game, shuffled=False):
        self.game = game

        self.ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
        self.suits = [Spades, Clubs, Hearts, Diamonds]
        self.face_up = False

        self.create_deck(shuffled)


    def create_deck(self, shuffled=False):
          
        self.deck = []
        
        for suit in self.suits:
            if trace: print(f"looping through suit: '{suit}'")

            for rank in self.ranks:
                if trace: print(f"looping through rank: '{rank}'")

                card = Card(suit, rank, self.game)
                self.deck.append(card)

        if shuffled:
            random.shuffle(self.deck)

        return self.deck
        
        
    def shuffle(self):
        random.shuffle(self.deck)


    def get_card(self):
        if len(self.deck) == 0:
            return "Deck is empty"
            
        return self.deck.pop()


    def is_empty(self):

        if len(self.deck) == 0: return True 


    def has_cards (self):

        return len(self.deck) > 0

    def __len__(self):
        return len(self.deck)
    
    
    def print(self):
        
        for card in self.deck:
            print(card)


if __name__ == "__main__":
    deck = Deck()
    # deck.print ()

    # deck.shuffle()
    # deck.print()

    # deck.create_deck()
    # deck.print()

    # print(deck.get_card())
    # deck.print()
        
