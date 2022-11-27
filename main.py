from rps import *
import os

logo = '''
  ___ ___  _____      _____ ___ 
 | _ \\ _ \\/ __\\ \\    / / __/ __|
 |   /  _/\\__ \\\\ \\/\\/ /| _|\\__ \\
 |_|_\\_|  |___/ \\_/\\_/ |___|___/                                
'''

print(logo)

homepath = os.path.expanduser('~')

mode = 'normal'

games_played = 0

games_won = 0
games_lost = 0
games_tied = 0

rating_user = 100
rating_computer = 100

highest_rating_user = rating_user
highest_rating_computer = rating_computer

# first-time check
if os.path.exists(homepath + '\\.novc\\rpswes'):
    # load stuff here
    pass
else:
    # The game is likely being opened for the first time.
    # The environment gets prepared for additions in later versions.
    print('Use x or start to star a game, stats to view your stats,\nc to clear and q to quit! Use mode to toggle between the two modes.\n')
    if os.path.exists(homepath + '\\.novc'):
        if os.path.exists(homepath + '\\.novc\\rpswes'):
            pass
        else:
            os.mkdir(homepath + '\\.novc\\rpswes')
    else:
        os.mkdir(homepath + '\\.novc')
        os.mkdir(homepath + '\\.novc\\rpswes')

# main loop
while True:
    cmd = input('>>> ')

    if cmd == 'c':
        clear()

    elif cmd == '' or cmd == ' ':
        continue

    elif cmd == 'start' or cmd == 'x':
        if mode == 'normal':
            result = run_round()

            if result == 0:
                games_won = add(games_won, 1)
                new_rating_user = rating_user + win_plus()

                if new_rating_user > highest_rating_user:
                    highest_rating_user = new_rating_user

                rating_user = new_rating_user
                rating_computer = rating_computer - loss_minus()
            if result == 1:
                games_lost = add(games_lost, 1)     
                new_rating_computer = rating_computer + win_plus()           
                
                if new_rating_computer > highest_rating_computer:
                    highest_rating_computer = new_rating_computer

                rating_computer = new_rating_computer
                rating_user = rating_user - loss_minus()
            if result == 2: games_tied = add(games_tied, 1)

            games_played = add(games_played, 1)

            if rating_user < 100: rating_user = 100
            if rating_computer < 100: rating_computer = 100
        if mode == 'impossible': run_round_impossible()

    elif cmd == 'mode':
        if mode == 'normal':
            print('Set the mode to', red('IMPOSSIBLE') + '.')
            mode = 'impossible'
        else:
            print('Set the mode to', green('NORMAL') + '.')
            mode = 'normal'

    elif cmd == 'stats':
        clear()
        get_stats(rating_user, rating_computer, highest_rating_user, highest_rating_computer, games_won, games_lost, games_tied, games_played)

    elif cmd == 'q' or cmd == 'quit' or cmd == 'exit':
        quit()

    else:
        err(f'No command named {cmd}.')