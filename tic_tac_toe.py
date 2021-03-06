from random import randint
import traceback
import copy

"""


Start with an empty grid of 3x3
2 Players are taking turns, place their symbol (x or o) on the grid
if someone gets 3 in a row, then he wins
if the grid is full and no one wins, then it is a draw
The game consists of many sets, count score using the wins
"""
      
   

def displayBoard(board):
    for i in range(0, len(board)):
        
        for j in range(0, len(board[i])):
            c = board[i][j]
            print(c, end=' |')
       
        print('')

def isBoardIsFull(board):
    total = 0
    for row in board: 
        total = total + row.count('X')+ row.count('O')

    return total == len(board)**2
   


def humanTurn(board):
    done = isBoardIsFull(board)
    N = len(board)
    while not done:
      
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
    



def score(board, i, j):
    
    '''
    returns a score evaluating the value of playing as the computer on cell i,j in board

    '''

    # make it computer_win*1000 + player_block*900
    if i > len(board) or i < 0 or j > len(board[i]) or j < 0:
        return 0

    if board[i][j] != ' ':
        return 1

    # the computer wins if he places it in cell i,j is the max score possible
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = 'O' 
    
    if checkBoardForWinner(board_copy) == -2:
        return 1000


    # if the human wins if he places it in cell i,j is the next best score
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = 'X'
    if checkBoardForWinner(board_copy) == -1:
        return 900
    
    count_o = 0
    count_x = 0
     #horizontal wins human player 

    row = board[i]
    count_o += row.count('O')
    count_x += row.count('X')
    #vertical
        
    
    column = [board[j][i] for j in range(len(board[i]))]
    count_o += column.count('O')
    count_x += column.count('X')

    # diagonals 
    if i == j:
        diag2 = [ row[i] for i, row in enumerate(board) ]
        count_o += diag2.count('O')
        count_x += diag2.count('X')

    if i == len(board)-j-1:
        diag = [ row[-i-1] for i,row in enumerate(board) ]
        count_o += diag.count('O')
        count_x += diag.count('X')


    return count_o*20 - count_x*10 + randint(1,6)


# returns the [i,j] coordinates on the board the computer should play, basically the coords of the cell with max score (using the function score)
def computer_choice(board):
    '''
    returns position that contains the maximun score on the board
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
                score_t = score(board, i, j) # returns value of cell
                if score_t > max:
                    max = score_t
                    max_ij = [i, j] #index that contains max score
    return max_ij
    #let computer choose an open space, then assign a score to each move, and take whichever one is open

def computerTurn(board):
    done = isBoardIsFull(board)
    while not done:

        computerChoice = computer_choice(board)
        
        if board[computerChoice[0]][computerChoice[1]] == ' ':
            board[computerChoice[0]][computerChoice[1]] = 'O'
            break
    done = True
            
    


def check_array_for_winner(diag): 
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


# return empty board of NxN - 
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


        computerTurn(board)
      
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
        print("Player Score: {} | Computer Score: {} ".format( human_total, computer_total))
        break

N = 3
human_total = 0
computer_total= 0 
restart_game = 'C'
while restart_game == 'C':
    new_board = clearBoard(N) 
    start_game(new_board)
    restart_game = input('Enter Q to quit or C to continue: ')


