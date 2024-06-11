def compare(human, dealer):
    """chechking who wins.

    Args:
        human (int): human score
        dealer (int): CPU score

    Returns:
        -1/0/1: decide who win -1:dealer 0:draw 1:human
    """
    if human.score > 21:
        print ("{} Busted!".format(human.name))
        return (-1)
    elif dealer.score > 21 :
        print("{} Busted!".format(dealer.name))
        return (1)
    elif dealer.score ==  human.score  :
        print("Both equal NO WIN!")
        return (0)
    elif human.score == 21 :
        print("{} BlackJACK!!".format(human.name))
        return (1)
    elif dealer.score == 21 :
        print("{} BlackJACK!!".format(dealer.name))
        return(-1)
    elif human.score - dealer.score > 0 :
        print("{} Wins!".format(human.name))
        return (1)
    elif human.score - dealer.score < 0 :
        print("{} Win!".format(dealer.name))
        return (-1)