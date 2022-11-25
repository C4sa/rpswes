from rps.corefunc import *
from rps.color import *
import random

options = ['r', 'p', 's']

def run_round():
    print('Rock, paper, scissors! Enter your choice (r/p/s):')
    user_choice = input('>> ')

    # validity check
    if user_choice == 'r' or user_choice == 'p' or user_choice == 's': valid = True        
    else: valid = False    

    # computer choice
    computer_choice = random.choice(options)

    # choices
    if valid:
        # converting
        if user_choice == 'r': user_choice = 'rock'
        if user_choice == 'p': user_choice = 'paper'
        if user_choice == 's': user_choice = 'scissors'

        if computer_choice == 'r': computer_choice = 'rock'
        if computer_choice == 'p': computer_choice = 'paper'
        if computer_choice == 's': computer_choice = 'scissors'

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

# types: 0: win, 1: loss, 2: tie
def announce(type, p1choice, p2choice):
    if type == 0: print(green('VICTORY!'), f'You selected {green(p1choice)}, computer picked {red(p2choice)}.')
    if type == 1: print(red('DEFEAT!'), f'You selected {red(p1choice)}, computer picked {green(p2choice)}.')
    if type == 2: print(gray('TIE!'), f'Both you and the computer selected {yellow(p2choice)}.')