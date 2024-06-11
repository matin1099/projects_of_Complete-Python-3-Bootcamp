from random import shuffle 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    """Card class:
    create 52  card with value

    """
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    """
    Create Deck of cards for playing
    will create full deck at  first use
    will suffle deck
    willremove dealed cards
    """
    def __init__(self):
        self.Newdeck()

    def Newdeck(self):
        """
        create a new deck
        Shuffling cards
        """
        self.all_card = []
        for i in suits:
            for j in ranks:
                self.all_card.append(Card(i,j))
        shuffle(self.all_card)

    def dealed(self):
        """Dealing a card and remove last card.
        """
        return(self.all_card.pop(-1))
