from rps import *
import os
import pickle

os.system('color')                  # colorization compatibility for windows 10 users
                                    # (without this line, the terminal displays the
                                    # escape code in regular terminals, I use WT (windows
                                    # terminal))

logo = '''
  ___ ___  _____      _____ ___ 
 | _ \\ _ \\/ __\\ \\    / / __/ __|
 |   /  _/\\__ \\\\ \\/\\/ /| _|\\__ \\
 |_|_\\_|  |___/ \\_/\\_/ |___|___/                                
'''

print(logo)

homepath = os.path.expanduser('~')
savepath = homepath + '\\.novc\\rpswes\\player.dat'

mode = 'normal'

games_played = 0

games_won = 0
games_lost = 0
games_tied = 0

rating_user = 100
rating_computer = 100

title_library = []
title = ''

highest_rating_user = rating_user
highest_rating_computer = rating_computer

achv_completed = 0
achv_completed_list = []
achv_uncompleted_list = []

def reset():
    global games_played, games_won, games_lost, games_tied, rating_user, rating_computer, title_library, title, highest_rating_user, highest_rating_computer, achv_completed, achv_completed_list, achv_uncompleted_list

    clear()
    confirm = input(red('DANGER ZONE!\n') + 'Please only reset your savefile if you know what you\'re doing\nand you are absolutely 100% sure! After you do, ' + red('THERE IS NO GOING BACK!') + '\n\nAre you sure? ' + gray('y/n\n'))
    if confirm == 'y':
        games_won = 0
        games_lost = 0
        games_tied = 0

        rating_user = 100
        rating_computer = 100

        title_library = []
        title = ''

        highest_rating_user = rating_user
        highest_rating_computer = rating_computer

        achv_completed = 0
        achv_completed_list = []
        achv_uncompleted_list = []

        save_progress()

        clear()
        print(red('ALL STATISTICS AND VARIABLES WERE RESET.'))
        time.sleep(1)
        clear()
    else:
        clear()
        print(yellow('Canceling reset...'))
        time.sleep(1)
        clear()

def title_check():
    global title_eligibility

    if highest_rating_user >= 2200: title_library.append('nm')
    if highest_rating_user >= 2400: title_library.append('lm')
    if highest_rating_user >= 2600: title_library.append('cm')
    if highest_rating_user >= 3000: title_library.append('gm')

def save_progress():
    with open(savepath, 'wb') as handle:
        pickle.dump([games_played, games_won, games_lost, games_tied, rating_user, rating_computer, highest_rating_user, highest_rating_computer, title, title_library, achv_completed, achv_completed_list, achv_uncompleted_list], handle, protocol=pickle.HIGHEST_PROTOCOL)

# savefile
if not os.path.exists(savepath):
    f = open(homepath + '\\.novc\\rpswes\\player.dat', 'x')
    save_progress()
    f.close()

# saving/loading progress into file
def load_progress():
    global games_played, games_won, games_lost, games_tied, rating_user, rating_computer, highest_rating_user, highest_rating_computer, title, title_library, achv_completed, achv_completed_list, achv_uncompleted_list

    if os.stat(savepath).st_size == 0:
        print('@@@ new player or corrupt savefile')
    else:
        try:
            with open(savepath, 'rb') as handle:
                games_played, games_won, games_lost, games_tied, rating_user, rating_computer, highest_rating_user, highest_rating_computer, title, title_library, achv_completed, achv_completed_list, achv_uncompleted_list = pickle.load(handle)
        except:
            print(yellow('There was an issue with your savefile, so for now, it couldn\'t be opened.\nI am working on resolving this issue.'))       

# first-time check
if os.path.exists(homepath + '\\.novc\\rpswes'):
    load_progress()
else:
    # The game is likely being opened for the first time.
    # The environment gets prepared for additions in later versions.
    print('Use x or start to start a game, stats to view your stats,\nc to clear and q to quit! Use mode to toggle between the two modes.\n')
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
    title_check()
    save_progress()
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

            save_progress()
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
        get_stats(rating_user, rating_computer, highest_rating_user, highest_rating_computer, games_won, games_lost, games_tied, games_played, title)

    elif cmd == 'nm':
        if 'nm' in title_library and title != 'nm':
            print(cyan('You equipped your New Master [NM] title!'))
            title = 'nm'
        elif 'nm' not in title_library:
            print(red('You don\'t have this title in your title inventory!'))
        else:
            print(yellow('You already have this title equipped!'))

    elif cmd == 'lm':
        if 'lm' in title_library and title != 'lm':
            print(cyan('You equipped your Local Master [LM] title!'))
            title = 'lm'
        elif 'lm' not in title_library:
            print(red('You don\'t have this title in your title inventory!'))
        else:
            print(yellow('You already have this title equipped!'))

    elif cmd == 'cm':
        if 'cm' in title_library and title != 'cm':
            print(cyan('You equipped your Casual Master [CM] title!'))
            title = 'cm'
        elif 'cm' not in title_library:
            print(red('You don\'t have this title in your title inventory!'))
        else:
            print(yellow('You already have this title equipped!'))

    elif cmd == 'gm':
        if 'gm' in title_library and title != 'gm':
            print(cyan('You equipped your Grandmaster [GM] title!\nThis is the highest title obtainable (so far)!'))
            title = 'gm'
        elif 'gm' not in title_library:
            print(red('You don\'t have this title in your title inventory!'))
        else:
            print(yellow('You already have this godly title equipped!'))

    elif cmd == 'q' or cmd == 'quit' or cmd == 'exit':
        save_progress()
        quit()

    elif cmd == 'reset':
        reset()

    else:
        err(f'No command named {cmd}.')