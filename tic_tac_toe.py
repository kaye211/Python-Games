from random import randint
import traceback

"""


Start with an empty grid of 3x3
2 Players are taking turns, place their symbol (x or o) on the grid
if someone gets 3 in a row, then he wins
if the grid is full and no one wins, then it is a draw
The game consists of many sets, count score using the wins
"""
      
   


# make it not explicit

def displayBoard(board):
    for i in range(0, len(board)):
        #start of row printing
        for j in range(0, len(board[i])):
            c = board[i][j]
            print(c, end=' |')
        #end of row printing
        print('')
    

# implement me
def isBoardIsFull(board):
    total = 0
    for row in board: 
        total = total + row.count('X')+ row.count('O')

    return total == len(board)**2
   


def humanTurn(board):
    done = isBoardIsFull(board)
    N = len(board)
    while not done:
       # if checkBoardForWinner(board) != -2: #to stop human from playing after compter wins
        humanInput = input('Choose an X value (0-%d) (0-%d): ' % (N-1, N-1)) 
                

        try:
            somevariable = humanInput.split()  
            row = somevariable[0]
            column = somevariable[1]
    
            if board[int(row)][int(column)] != ' ':
                print(row, column)  
                print ("Please choose another row/column")
            else: 
                board[int(row)] [int(column)] = 'X'
                break
                    

        except Exception as e:
            print("Please choose a number between 0 -3")
            print(e)
            traceback.print_exc()
    

import copy
# returns a score evaluating the value of playing as the computer on cell i,j in board
def score(board, i, j):
    # if the computer wins if he places it in cell i,j is the max score possible
    bcopy = copy.deepcopy(board)
    bcopy[i][j] = 'O'
    # check

    # if the human wins if he places it in cell i,j is the next best score
    bcopy = copy.deepcopy(board)
    bcopy[i][j] = 'X'
    # check
    
    # next it should proportionall to how many computer chars are in the same row, column or diagonals

    # last should be random score less than the cases above

    return randint(0, 1000)

# A = [100, 0, 1, 5, 10 ,6 , 8 , 100, 9]
# sum = 0
# for a in A:
#     sum = sum + a

# max = A[0]
# for a in A:
#     if a >= max:
#         max = a

# max = A[0]
# max_i = 0
# for i in range(0, len(A)):
#     if A[i] >= max:
#         max = A[i]
#         max_i = i


# returns the [i,j] coordinates on the board the computer should play, basically the coords of the cell with max score (using the function score)
def computer_choice(board):
    '''
    choses the maximun score on the board
    '''
    '''

    scores = []
    for i in range(len(board)):
        sublist = []
        for j in range(len(board[i])):
            score_t = score(board, i, j) #function tells score for a cell i,j
            sublist.append(score_t)
        scores.append(sublist)

    max = scores[0][0]
    max_ij = [0,0]
    for i in range (0, len(scores)):
        for j in range(0, len(scores[i])):
            if scores[i][j] == ' ':
                if scores[i][j] > max:
                    max = scores[i][j]
                    max_ij = [i, j]
    '''
    max = -1000
    max_ij = [0,0]
    for i in range (0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == ' ':
                score_t = score(board, i, j)
                if score_t > max:
                    max = score_t
                    max_ij = [i, j]
    #set max_score to 0 and max_cell to Rand
    #go over every cell in the board, and for cell that is empty, get a score and if it more than the max score save it as the max_cell for now
    return max_ij
    #let computer choose an open space, then assign a score to each move, and take whichever one is open

def computerTurn(board):
    done = isBoardIsFull(board)
    while not done:
    #while True:

        #populate board with number 
        computerChoice = computer_choice(board)
        #print (computerChoice)
        
        if board[computerChoice[0]][computerChoice[1]] == ' ':
            board[computerChoice[0]][computerChoice[1]] = 'O'
            break
    done = True
            
    


def check_array_for_winner(diag): #diag name to row/column
    N = len(diag)
    
    if diag.count('X') == N:
        return -1
    if diag.count('O') == N:
        return -2
    return 0

def checkBoardForWinner(board):
  
    #horizontal wins human player 
    for i in range(0, len(board)): #columns 3
        row = board[i]
        check_row = check_array_for_winner(row)
        if check_row:
            return check_row

    #vertical
        
    for i in range(len(board[0])):
        column = [board[j][i] for j in range(len(board[i]))]
        check_column = check_array_for_winner(column)
        if check_column:
            return check_column

    # diagonals 
    diag2 = [ row[i] for i, row in enumerate(board) ]
    check_diag = check_array_for_winner(diag2)
    if check_diag:
        return check_diag
    diag = [ row[-i-1] for i,row in enumerate(board) ]
    check_diag = check_array_for_winner(diag)
    if check_diag:
        return check_diag
    return 0


# return empty board of NxN
def clearBoard(N):
    board = [ [' ', ' ', ' ' ], 
              [' ', ' ', ' ' ],
              [' ', ' ', ' ' ]]

    return board



def start_game(board):
    global human_total, computer_total

    while not isBoardIsFull(board):
        displayBoard(board)
        humanTurn(board)
     
        check_result = checkBoardForWinner(board) 
        if check_result == -1:
            human_total = human_total +  1
            displayBoard(board)
            print ("Human player wins")
            break     
        elif check_result == -2:
            computer_total = computer_total +  1
            displayBoard(board)
            print("Computer wins")
            break



        #    elif check_result == -1 or check_result == -2: #why doesnt this if statement work?
        #         break



        # should also check for full.. and do something with the check for winner result, use temps
        computerTurn(board)
        #displayBoard(board)
        #check for a winner
        check_result = checkBoardForWinner(board) 
        if check_result == -1:
            displayBoard(board)
            print ("Human wins")
            break
        elif check_result == -2:
            displayBoard(board)
            print("Computer wins")
            computer_total = computer_total +  1
            break


    while checkBoardForWinner(board):
        print("Score is human: ", human_total, computer_total)
        break

N = 3
human_total = 0
computer_total= 0 
restart_game = 'c'
while restart_game == 'c':
    new_board = clearBoard(N) 
    start_game(new_board)
    restart_game = input('Enter Q to quit or C to continue: ')


# display improved
# N = 4, N = 5
# computer smart
#use scores to determine where computer plays
