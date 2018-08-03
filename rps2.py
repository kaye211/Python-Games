
from random import randint
"""
Rock Paper Scissors Game Implementation
Rock smashes scissors
Scissors cuts paper
Paper covers rock
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


def player_choice(): #does this need to take in a parameter?
    """
    This takes in the human players input and returns an integer value
    0 - rock
    1 - paper
    2 - scissors

    """
    done = True
    while done:
        choice = input("Please choose rock, paper or scissors: ")
        if  choice !='rock' and choice != 'paper' and choice !='scissors': #confused, why does and work here should it be or?
            print("Invalid choice, please choose either rock, paper or scissors")
        else:
         return name_to_number(choice)
         #break  #why is break reachable with a print but unreachablle with return?
        
def computer_choice():
    """
    returns a randomly choosen integer - 0, 1, 2 for computer choice"
    """
    check= randint(0, 2)
    print(number_to_name(check))
    return check 

computer_choice()

player1choice = player_choice()
player2choice= computer_choice()



# player1 = 4  #will be whoevergoes first

def play_game(player1 , player2):
   
    if player1choice == 0 and player2choice == 2:
       print("rock smashes scissors, " + ' ' + player1+ 'wins')
       
    elif player1choice == 2 and player2choice == 1:
        print("Scissors cuts paper, the winner, " + ' ' + player1+ 'wins')
    elif player1choice ==1 and player2choice == 0:
        print("Paper covers rock, "+  ' ' + player1+ 'wins')
    elif player2choice == 0 and player1choice == 2:
       print("Rock smashes scissors, " + ' ' +  player2+ 'wins')
       
    elif player2choice == 2 and player1choice == 1:
        print("Scissors cuts paper,  "+ ' ' + player2+ 'wins')
    elif player2choice == 1 and player1choice == 0:
        print("Paper covers rock, " + ' ' + player2 + 'wins') 
    else:
        print("There is a Tie")

play_game(player1= 'human', player2 = 'human')
    
def is_First():
    return(randint(0, 1))

    
#Need to figure out how to select a random choice
# turn = is_First()
# humanP = player_choice()
# if turn == 0: #human plays first, player1 = human
#     player_choice()
# else:
#     computer_choice()


    
# human_player = 3
# computer_player = 4
# start_game = True
# while start_game():
#     if randint(3, 4) == 3:
#         #human plays first
#     else
#         #computer p;ats 
# play_game(human_player, computer_player):
#     result =
#     print(result) 

#     if  result == 3: 
#         print(result) 
#         player_choice()
#     else:
#         print(result, 2) 
#         computer_choice()
#         break

#when I call play_game(), I will call it with human_player and compuer_Plater

#randonmly select who goes first
# 1 for human , 2 for computer
# if    randint(0, 1) == 1:
#               play_game == computer:
#       else == human

#test
# print(name_to_number('rock'))  # output = 0
# print(name_to_number('paper'))  # output = 1
# print(name_to_number('scissors'))  # output = 2

# print(number_to_name(0))  # output = rock
# print(number_to_name(1))  # output = paper
# print(number_to_name(2)) # output = scissors
# print(number_to_name(3))
#player_choice()
#print(player_choice())
#print(computer_choice())



      