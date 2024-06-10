"""
* The game needs to have one player versus an automated dealer.
* The player can stand or hit.
* The player must be able to pick their betting amount.
* You need to keep track of the player's total money.
* You need to alert the player of wins, losses, or busts, etc...

And most importantly:

* **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**

"""

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
        self.all_card = []
        for i in suits:
            for j in ranks:
                self.all_card.append(Card(i,j))
        self.Shuffle()

    def Shuffle(self):
        """Shuffling cards
        """
        shuffle(self.all_card)

    def dealed(self):
        """Dealing a card and remove last card.
        """
        return(self.all_card.pop(-1))

class Player():
    
    """
    player class
    Choose to be  CPU or Human
    have money
    can get card (hit) or decline (stay)
    """
    def __init__(self,name:str, money:int, cpu=True):
        self.name = name
        self.hold = []
        self.score = 0
        self.money = 0
        self.cpu = cpu

    def __str__(self):
        return print(self.name, "have $", self.money+".")
      
class Bet :
    """class to get bet mone and check for valid money
    """
    def __init__(self):
        pass

    def bet(self, player):
        print(player.name, "place your bet:")
        while True:
            amount = int(input())
            if amount <= player.money:

                print ("bet accepted")
                return amount
            else:
                print("Selected bet is more than you have!\nPlace your bet:")


play_deck = Deck()

