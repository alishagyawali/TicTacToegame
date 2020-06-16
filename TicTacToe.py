lists = [' ']*10
# lists[0] = '#'
def board():
    print(lists[1]+ '|' + lists[2] + '|' + lists[3])
    print('---------')
    print(lists[4] + '|' + lists[5] + '|' + lists[6])
    print('----------')
    print(lists[7]+'|' +lists[8] + ' |' + lists[9])

def win(mark):
    return ((lists[1] == lists[2] == lists[3] == mark) or (lists[4] == lists[5] == lists[6] == mark)
    or (lists[7] == lists[8] == lists[9] == mark) or (lists[1] == lists[5] == lists[9]== mark)or (lists[3] == lists[5] == lists[7] == mark))
def blank(position):
    return lists[position] == ' '
def game():
    choose = input("enter ur choice 'X' or 'O' ").upper()
    
    
    turn = "first"
    
    while(1):

        if(' ' not in lists and (turn == "first" or turn =="second")):
            print('Draw')
            break
        elif (turn == "first"):
            print("player 1 turn ")
            position = int(input("enter ur postiion "))
            if(blank(position)):
                lists[position] = 'X'
                board()
            else:
                print("Give correct position")
                
                position = int(input("enter ur position "))
            if(win('X')):
                print("player 1 wins")
                break
            else:
                turn = "second"
        elif (turn == "second"):
            print("player 2 turn")
            position = int(input("enter ur position "))
            if(blank(position)):
            
                lists[position] = "O"
                board()
            else:
                print("Give correct position")
                position = int(input("enter ur position "))
            if(win('O')):
                print("player 2 wins")
                break
            else:
                turn = "first"

game()
lists = [' ']*10
replay = input("Replay 'Y' of 'N'").upper()
if(replay == 'Y'):
    game()
else:
    print("thank you")