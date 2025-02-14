def Display_output(Bord):

    print(Bord[9]+'|'+Bord[8]+'|'+Bord[7])
    print(Bord[6]+'|'+Bord[5]+'|'+Bord[4])
    print(Bord[3]+'|'+Bord[2]+'|'+Bord[1])

def Player_marker():
    marker=' '
    while marker!='O' and marker!='X':
        marker=input("Player First choose Marker :O and X").upper()
    if marker=='O':
        return ('O','X')
    return ('X','O')  
            
def place_marker(Bord,marker,position):
    Bord[position]=marker

def win_check(bord,mark):
    return ((bord[1]==mark and bord[2]==mark and bord[3]==mark) or
            
            
            (bord[4]==mark and bord[5]==mark and bord[6]==mark) or
            (bord[7]==mark and bord[8]==mark and bord[9]==mark) or
            (bord[1]==mark and bord[4]==mark and bord[7]==mark) or
            (bord[2]==mark and bord[5]==mark and bord[8]==mark) or
            (bord[3]==mark and bord[6]==mark and bord[9]==mark) or
            (bord[1]==mark and bord[5]==mark and bord[9]==mark) or
            (bord[3]==mark and bord[5]==mark and bord[7]==mark) 
           
            
            )



import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
    

def space_check(Bord,position):
    return Bord[position]==' '



def Bord_is_full(Bord):
    for i in range(1,10):
        if space_check(Bord,i):
            return False
    return True

def player_choice(Bord):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] and not space_check(Bord,position):
        position=int(input("Enter Number range 1 to 9"))
    return position
    
def replay():
    choice=input("If replay Game press YES else press NO").upper()
    return choice=="YES"



print("welcome Tic Tac Toe")
while True:
    this_list=[' ']*10
    Player1_marker,Player2_marker=Player_marker()
    print('hi')
    turn=choose_first()
    print(turn+' will go First') 
    

    play_game=input("Ready to play? Y or N").upper()

    if play_game=='Y':
        game_on=True
    else:
        game_on=False


       

    while game_on:
        print(turn+'Turn')
        if turn=='Player 1':
            Display_output(this_list)
            position=player_choice(this_list)
            place_marker(this_list,Player1_marker,position)

            if win_check(this_list,Player1_marker):
                Display_output(this_list)
                print("Player 1 Win!!!")
                game_on=False
            else:
                if Bord_is_full(this_list):
                    Display_output(this_list)
                    game_on=False
                else:
                    turn='Player 2' 
        else:             
             Display_output(this_list)
             position=player_choice(this_list)
             place_marker(this_list,Player2_marker,position)

             if win_check(this_list,Player2_marker):
                Display_output(this_list)
                print("Player 2 Win!!!")
                game_on=False
             else:
                if Bord_is_full(this_list):
                    Display_output(this_list)
                    game_on=False
                else:
                    turn='Player 1' 


