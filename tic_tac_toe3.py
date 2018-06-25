from random import randint
"""
Start with an empty grid of 3x3
2 Players are taking turns, place their symbol (x or o) on the grid
if someone gets 3 in a row, then he wins
if the grid is full and no one wins, then it is a draw
The game consists of many sets, count score using the wins
"""

board =  [' ', ' ', ' ' , ' ', ' ', ' ' , ' ', ' ', ' ' ] 
          
          
        
         
   


def displayBoard(board):
    print(board[6]+ '|' + board[7]+ '|'+ board[8])
    print('-----')
    print(board[3]+ '|' + board[4]+ '|'+ board[5])
    print('-----')
    print(board[0]+ '|' + board[1]+ '|'+ board[2])

def checkBoardIsFull():
   return True
#BoardIsFull= checkBoardIsFull()


def startPlaying(board):
    displayBoard(board)
    
    while checkBoardIsFull() == True:
        humanInput = input('Choose your next position (0-9): ') #why doesnt it work to put try b4 human input?

        
        try:
            board[int(humanInput)] = 'X'
            displayBoard(board)
            
        except:
            print("Please choose a number between 0 -9")
           # break
    #else:
       # print('board is full')
   


    
    while checkBoardIsFull() == True:
        #pick a number between 0 - 9 
        #if number has been chosen by human pick another number
        #populate board with number 
        computerChoice = randint(0, 8)
        while computerChoice != int(humanInput):
            board[computerChoice]='O'
            break
        
startPlaying(board)


def checkBoardForWinner():
    #for i in board:

    pass



def clearBoard():
    #clears board for new game
    pass


clearBoard()
'''
while checkBoardIsFull():
    humanTurn(board)
    computerTurn(board)
    #check for a winner

    if checkBoardForWinner == 0:
        print ("Human wins")
    elif checkBoardForWinner == 0:
        print("Computer wins")
    else:
        print("try again")
        
'''






"""
FizzBuzz, for every number in [0,100] if the number is 
wholy divided by 3 then print 'Fizz' if it is wholy divided 
by 5 then print 'Buzz' if it is both wholy divided by 3 and 5 print FizzBuzz
else just print the number

example:
1
2
Fizz
4
Buzz
Fizz
7
..
"""

def fizzbuzz():
    for i in range(0, 101):
        if i % 3==0 and i % 5==0:
            print ('FizzBuzz')
        elif i % 3==0:
            print ('Fizz')
        elif i % 5==0:
            print('Buzz')
        else:
            print(i)

