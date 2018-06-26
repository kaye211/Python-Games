
from random import randint
"""
Rock Paper Scissors Game Implementation
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
    3 - scissors
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return  'paper'
    elif number == 2:
        return 'scissors'
    else:
        return 'invalid choice'


def player_choice(): #does this need to take in a parameter?
    done = True
    while done:
        choice = input("Please choose rock, paper or scissors: ")
        if  choice !='rock' and choice != 'paper' and choice !='scissors': #confused, why does and work here should it be or?
            print("Invalid choice, please choose either rock, paper or scissors")
        else:
         return choice
         #break  #why is break reachable with a print but unreachablle with return?
      
def computer_choice():
    """
    returns a randomly choosen integer - 0, 1, 2 for computer choice"
    """
    return randint(0, 2)

def play_game(player):
    

    
    

#test
# print(name_to_number('rock'))  # output = 0
# print(name_to_number('paper'))  # output = 1
# print(name_to_number('scissors'))  # output = 2

# print(number_to_name(0))  # output = rock
# print(number_to_name(1))  # output = paper
# print(number_to_name(2)) # output = scissors
# print(number_to_name(3))
#player_choice()
# print(player_choice('rock'))
print(computer_choice())



      