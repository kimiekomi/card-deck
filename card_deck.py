#! /usr/bin/env python3

import random

debug = True
trace = True

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def display(self):
        print(f"'{self.rank}' of '{self.suit}'")


class Deck():
    def __init__(self):
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        suits = [1, 2, 3, 4]
        
        self.card_deck = []

        for rank in ranks:
            if trace: print(f"looping through rank: '{rank}'")

            for suit in suits:
                if trace: print(f"looping through suit: '{suit}'")
                
                card = Card(rank, suit)
                self.card_deck.append(card)


    def shuffle(self):
        self.copy_deck = self.card_deck.copy()
        random.shuffle(self.copy_deck)


    def deal(self):
        return self.copy_deck.pop()


    def reveal(self):
        for card in self.copy_deck:
            card.display()


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.deal()
    deck.reveal()

