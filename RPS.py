
from random import randint
"""
Rock Paper Scissors Game Implementation
Rock smashes scissors
Scissors cuts paper
Paper covers rock
"""

"""
improvement suggestions
    get rid of the numbers, just use the strings directly
    keep score of the wins..
"""

def name_to_number(name):
    """
    Takes string name and converts to corresponding number
    Rock - 0
    paper - 1
    scissors - 2

    """

    if name == 'rock':
        return 0
    elif name == 'paper':
        return 1
    elif name == 'scissors':
        return 2
    else:
        return 3
        

   
def number_to_name(number):
    """
    Takes an integer number (0, 1, 2)
    and converts to corresponding string
    0 - rock
    1 - paper
    2 - scissors
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return  'paper'
    elif number == 2:
        return 'scissors'
    else:
        return 'invalid choice'


def player_choice(): 
    """
    This takes in the human players input and returns an integer value
    0 - rock
    1 - paper
    2 - scissors

    """
    done = True
    while done:
        choice = input("Please choose rock, paper or scissors: ")
        
        if  choice !='rock' and choice != 'paper' and choice !='scissors': 
            print("Invalid choice, please choose either rock, paper or scissors")
        else:
            return name_to_number(choice)
      
        
def computer_choice():
    """
    returns a randomly choosen integer - 0, 1, 2 for computer choice"
    """
    return randint(0, 2)
  



def play_game(player1 , player2): 
    player1choice = player_choice()
    player2choice = computer_choice()
    print(player1 + ' choses ' + number_to_name(player1choice) )
    print(player2 + ' choses ' + number_to_name(player2choice) )

    if player1choice == 0 and player2choice == 2:
        print("Rock smashes scissors, " + player1+  ' ' + 'wins')
        return 0
       
    elif player1choice == 2 and player2choice == 1:
        print("Scissors cuts paper, " + player1 +  ' ' +'wins')
        return 0

    elif player1choice == 1 and player2choice == 0:
        print("Paper covers rock, "+ player1+  ' ' + 'wins')
        return 0

    elif player2choice == 0 and player1choice == 2:
        print("Rock smashes scissors, " +   player2+ '' + 'wins')
        return 1
       
    elif player2choice == 2 and player1choice == 1:
        print("Scissors cuts paper,  "+  player2+  ' ' +'wins')
        return 1

    elif player2choice == 1 and player1choice == 0:
        print("Paper covers rock, " + player2 +  ' ' + 'wins') 
        return 1

    else:
        print("There is a tie, try again")
        return 2 

player_total = 0
computer_total = 0
continue_game ='Y'
while continue_game == 'Y':
    game_result = play_game(player1= 'Player', player2 = 'Computer')
    if game_result  == 0:
        player_total = player_total + 1
    elif game_result  == 1:
        computer_total = computer_total + 1
    print("Scores")
    print("-----------")
    print("Human Score: {} | Computer Score: {} ".format(player_total, computer_total))
    continue_game = input('Enter Y to continue or any key to quit: ')

   
print("Scores are: Human: {} | Computer: {}". format(player_total, computer_total))
print("Thanks for playing!" ) 
  


    
    





      
