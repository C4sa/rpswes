from rps.game_normal import *

def run_round_impossible():
    print(red('IMPOSSIBLE MODE'), 'Rock, paper, scissors! Enter your choice (r/p/s):')
    user_choice = input('>> ')

    # validity check
    if user_choice == 'r' or user_choice == 'p' or user_choice == 's': valid = True        
    else: valid = False    

    # computer choice
    if user_choice == 'r': computer_choice = 'paper'
    if user_choice == 'p': computer_choice = 'scissors'
    if user_choice == 's': computer_choice = 'rock'

    # choices
    if valid:
        # converting
        if user_choice == 'r': user_choice = 'rock'
        if user_choice == 'p': user_choice = 'paper'
        if user_choice == 's': user_choice = 'scissors'

        # game
        if user_choice == computer_choice:
            announce(2, user_choice, computer_choice)

        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                announce(0, user_choice, computer_choice)
            else:
                announce(1, user_choice, computer_choice)

        elif user_choice == 'paper':
            if computer_choice == 'rock':
                announce(0, user_choice, computer_choice)
            else:
                announce(1, user_choice, computer_choice)

        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                announce(0, user_choice, computer_choice)
            else:
                announce(1, user_choice, computer_choice)

    else:
        err('Invalid choice! Available: r/p/s')