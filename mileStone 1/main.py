def start():
    print("""سلام به بازی دوز خوش اومدی. 
اینجا ما بازی دوز داریم که با دو تا بازیکن هست و شما باید از شماره ۱ الی ۹ رو به صورت لاتین وارد کنید تا مهرا  در اون مکان گذاشته شود.
صفحه دوز به این شکل است""")
    print('''
    1 | 2 | 3 
    __________
    4 | 5 | 6
    __________
    7 | 8 | 9

    ''')
    players = [(input("اسم بازیکن X :   "),"X"),(input("اسم بازیکن O :   "),"O")]

    return players
def duration(players_names):
    pind = 1
    isEND = False
    selected=['\n ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while not isEND:
        board(selected)

        pind = cycling(pind)

        selected = choose(players_names[pind], selected)

        isfinal, isEND, mark = isdone(selected)
    
    return mark, isfinal

        
        
def end_game(players_names, final, mark ):
    if final == "win":
        winner = players_names[0][0] if mark == "X" else players_names[1][0]
        fin_msg = "برد {}".format(winner)
    else:
        fin_msg = "تساوی"
    print("""پایان بازی:
          

          بازی بین {0} و {1} با نتیجه {2} به پایان رسید
          از این که با ما این بازی را امتجان کردید متشکرم.
          """.format(players_names[0][0], players_names[1][0], fin_msg))
def board(selected):
    """ نمایش وضعیت کنونی میز بازی

    Args:
        selected (list): selected and unselected places
    """
    print('''{0}
    {1} | {2} | {3} 
    __________
    {4} | {5} | {6}
    __________
    {7} | {8} | {9}

    '''.format(selected[0],
               selected[1],selected[2],selected[3],
               selected[4],selected[5],selected[6],
               selected[7],selected[8],selected[9],))
def cycling(player_index):
     return 1 if player_index == 0 else  0
def choose(player, places ):
    """انتخاب خانه برای بازیکن خوانده شده.

    Args:
        player (str): player in turn
        places (list, optional): _description_. Defaults to selected.

    Returns:
        list: updated places
    """
    not_Valid = True
    chosen = int(input("{}، خانه بعدی رو انتخاب کن".format(player[0])))
    while not_Valid:
        if places[chosen] != " ":
            chosen = int(input("اون مکان قبلا زده شده، خانه بعدی رو  دوباره انتخاب کن".format(player[0])))
        else  :
            places[chosen] = player[1]
            not_Valid = False

    return places
def isdone(selected):
    end = False
    mark=''
    # WIN
        if ((selected[1] == selected[2] == selected[3] and selected[1] != ' ') or
            (selected[4] == selected[5] == selected[6] and selected[4] != ' ') or
            (selected[7] == selected[8] == selected[9] and selected[7] != ' ') or
            (selected[1] == selected[4] == selected[7] and selected[1] != ' ') or
            (selected[2] == selected[5] == selected[8] and selected[2] != ' ') or
            (selected[3] == selected[6] == selected[9] and selected[3] != ' ') or
            (selected[1] == selected[5] == selected[9] and selected[1] != ' ') or
            (selected[3] == selected[5] == selected[7] and selected[3] != ' ')):
        final = 'win'
        if selected.count("X")> selected.count("O"):
            mark = "X"
        else:
            mark = "O"
        end = True
    elif ' ' in selected:
        #contineu
        final ="contineu"
        end = False   
    else:
        final ="draw"
        end = True
        #draw    
    return final, end, mark

    
#GAME
players_names = start()
mark, isfinal = duration(players_names)
end_game(players_names, isfinal, mark)
