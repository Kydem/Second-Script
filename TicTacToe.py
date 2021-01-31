import os
import time

BOARD = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
PLAYER = 1

#### WIN Flags ####
WIN = 1
DRAW = 2
RUNNING = 0
STOP = 1
###################
GAME = RUNNING
MARK = 'X'

#BOARD#
def DRAWBOARD():
    print(" %c | %c | %c " % (BOARD[1],BOARD[2],BOARD[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (BOARD[4],BOARD[5],BOARD[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (BOARD[7],BOARD[8],BOARD[9]))
    print("   |   |   ")

#Position Check#
def CheckPosition(x):
    if(BOARD[x] == ' '):
        return True
    else:
        return False 

#WIN Check#
def CheckWIN():
    global GAME
    #Horizontal condition#
    if(BOARD[1] == BOARD[2] and BOARD[2] == BOARD[3] and BOARD[1] != ' '):
        GAME = WIN
    elif(BOARD[4] == BOARD[5] and BOARD[5] == BOARD[6] and BOARD[4] != ' '):
        GAME = WIN
    elif(BOARD[7] == BOARD[8] and BOARD[8] == BOARD[9] and BOARD[7] != ' '):
        GAME = WIN
    #Vertical condition#
    elif(BOARD[1] == BOARD[4] and BOARD[4] == BOARD[7] and BOARD[1] != ' '):
        GAME = WIN
    elif(BOARD[2] == BOARD[5] and BOARD[5] == BOARD[8] and BOARD[2] != ' '):
        GAME = WIN
    elif(BOARD[3] == BOARD[6] and BOARD[6] == BOARD[9] and BOARD[3] != ' '):
        GAME = WIN
    #Diagonal condition#
    elif(BOARD[1] == BOARD[5] and BOARD[5] == BOARD[9] and BOARD[1] != ' '):
        GAME = WIN
    elif(BOARD[3] == BOARD[5] and BOARD[5] == BOARD[7] and BOARD[3] != ' '):
        GAME = WIN
    #DRAW condition#
    elif(BOARD[1]!=' ' and BOARD[2]!=' ' and BOARD[3]!=' ' and BOARD[4]!=' ' and BOARD):
        GAME==DRAW
    else:
        GAME=RUNNING 

print("Tic-Tac-Toe GAME Designed By Sourabh Samnai")
print("PLAYER 1 [x] --- PLAYER 2 [O}\n")
print()
print()
print("please wait...")
time.sleep(3)
while(GAME == RUNNING):
    os.system('cls')
    DRAWBOARD()
    if(PLAYER % 2 != 0):
        print("PLAYER 1's chance")
        MARK = 'X'
    else:
        print("PLAYER 2's chance")
        MARK = 'O'
    choice = int(input("Enter the position between [1-9] where you want to MARK : "))
    if(CheckPosition(choice)):
        BOARD[choice] = MARK
        PLAYER+=1
        CheckWIN()

os.system('cls')
DRAWBOARD()
if(GAME==DRAW):
    print("GAME DRAW")
elif(GAME==WIN):
    PLAYER-=1
    if(PLAYER%2!=0):
        print("PLAYER 1 WINs")
    else:
        print("PLAYER 2 WINs")

