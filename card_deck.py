#! /usr/bin/env python3

debug = True
trace = True

class CardDeck():

    def __init__(self):
        self.ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.suits = ["spades", "clubs", "hearts", "diamonds"]

        self.standard_deck = []

        suits_index = 0

        for i in range(len(self.ranks)):
            if trace: print(f"looping through rank: '{self.ranks[i]}' and value: '{self.values[i]}'")

            # self.standard_deck.append([self.ranks[i], self.values[i]])

            for i in range(len(self.suits)):
                
                if suits_index <= len(self.suits):
                    if trace: print(f"looping through suit: '{self.suits[i]}'")
    
                    self.standard_deck.insert(2, self.suits[i])
        
                    suits_index += 1
    
                    if suits_index > 3:
                        suits_index -= 4
    
        print(self.standard_deck)

        # for card in self.standard_deck:
        #     for i in range(len(self.suits)):
                
        #         if suits_index <= len(self.suits):
        #             if trace: print(f"looping through suit: '{self.suits[i]}'")
    
        #             card.insert(2, self.suits[suits_index])
        
        #             suits_index += 1
    
        #             if suits_index > 3:
        #                 suits_index -= 4

        # print(self.standard_deck)
    


    def shuffle(self):
        pass


    def deal(self):
        pass


def play_cards():
    if debug: print("initialized create_deck()")
    
    card_deck = CardDeck()

    # card_deck.shuffle()

    return card_deck
    

    
if __name__ == "__main__":
    play_cards()

