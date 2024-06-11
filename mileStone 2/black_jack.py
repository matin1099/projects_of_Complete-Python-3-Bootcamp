"""
* The game needs to have one player versus an automated dealer.
* The player can stand or hit.
* The player must be able to pick their betting amount.
* You need to keep track of the player's total money.
* You need to alert the player of wins, losses, or busts, etc...

And most importantly:

* **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**

"""
from files.player import Player
from files.compare import compare
from files.deck import Deck

print("Welcome to BlackJack")
p1 = Player(input("Please Enter your Name:\t"), int(input("How much money you have?\t")), False)
p2 = Player("Dealer", p1.money)


while True:
    # Main game loop
    #break if END condition trigged

    # making bet and 
    # only human can bet
    deck = Deck() #Create cards
    bet_money = p1.bet()
    bet_money = p2.bet(bet_money)

    print("time to deal cards:")
    #passing Card and read both Human   
    p1.get_card(deck.dealed())
    p1.get_card(deck.dealed())
    p1.read()
    # getting card and read one dealer
    p2.get_card(deck.dealed())
    p2.read()
    p2.get_card(deck.dealed())


    #human/player choose to hit or stay
    print("now time to play!!!")
    respond = ''
    play_round = True
    while play_round:
        p1.read()
        respond = input("{} [H]it Or [S]tay?? ".format(p1.name))
        if respond in  ["h", "H",]:
            print("{} HITTED".format(p1.name))
            play_round =p1.hit(deck.dealed())
        elif respond in ["s", "S"]:
            print("{} STAYED".format(p1.name))
            play_round = False
        else:
            print("Bad choice")
            continue
            

            # dealer play
    print("Now dealer \n\n")
    respond = ''
    play_round = True
    while play_round:
        p2.read()
        if p2.score < 21 and p2.score < p1.score:
            print("{} HITTED".format(p2.name))
            play_round =p2.hit(deck.dealed())
        else:
            print("{} STAYED".format(p1.name))
            play_round = False            
   
    #choosing  winner and money returns
    winner = compare(p1, p2)
    if winner == 1:
        p1.win_bet(bet_money*2)
    elif winner == -1:
        p2.win_bet(bet_money*2)
    elif winner == 0 :
        p1.win_bet(bet_money)
        p2.win_bet(bet_money)
    
    # END conditions
    if p1.money == 0:
        print ("{} lose all of money. GAMEOVER".format(p1.name))
        break
    elif p2.money == 0:
        print ("{} lose all of money. GAMEOVER".format(p2.name))
        break
    
    # clear all changing for next round.
    print("NOW REDY FOR NEXT ROUND\n\n\n\n")
    p1.clear()
    p2.clear()
    bet_money = 0
    print("{} have {}.".format(p1.name,p1.money))
    print("{} have {}.".format(p2.name,p2.money))
