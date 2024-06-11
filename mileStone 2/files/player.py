class Player():
    
    """
    player class
    Choose to be  CPU or Human
    have money
    can get card (hit) or decline (stay)
    """
    def __init__(self,name:str, money:int, cpu=True):
        """__init__

        Args:
            name (str): Player Name
            money (int): starting money
            cpu (bool, optional): MUAT FALSE TO HUMAN PLAYS. is player atumated for hit. Defaults to True.
        """
        self.name = name.capitalize()
        self.hold = []
        self.score = 0
        self.money = money
        self.cpu = cpu
        print(self.name, "have $", str(self.money)+".")

    def bet(self,human_bet=0):
        """betting between players

        Args:
            human_bet (int, optional): for atumated players . Defaults to 0.

        Returns:
            bet_money: human betted
        """
        if human_bet ==0: 
            while True:
                amount = input("{} place your bet:".format(self.name))
                if int(amount) <= self.money:

                    print ("bet accepted")
                    self.money -= int(amount)
                    return int(amount)
                
                else:
                    print("Selected bet is more than you have!")
        else:
            self.money -= human_bet
            return human_bet
    def win_bet(self,win_money):
        """increse money over winning

        Args:
            win_money (int): win money
        """
        self.money += win_money

    def get_card(self,card):
        """Geting first 2 cards

        Args:
            card (cards): very first 2 cards
        """
        self.hold.append(card)
        
        self.score += card.value
    
    def read(self,):
        """printing now holding Cards

        Returns:
            END GAME : endgame conditions
        """
        print ("{} have :".format(self.name))
        for i in self.hold:
            print (i, sep=' ', end=', ', flush=True)
        print ("and scored {}.".format(self.score))
        if self.score > 21 :
            print("{} Have BUSTED.".format(self.name))
            return False
        else:
            return True       

    def hit(self, card):
        """asking for more cards

        Args:
            card (card): new card
        """
        if self.cpu == True:
            pass
        #moveed to main game scripts
        
            
        else:    
            self.hold.append(card)
            self.score += card.value
            self.read()

        
    def clear(self,):
        """cleaning holders
        """
        self.hold = []
        self.score = 0