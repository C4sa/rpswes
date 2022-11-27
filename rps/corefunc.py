import os
import time
from rps.color import *

fancy_exit_lines = [
                        'Checking save directory existence',
                        'Verifying stats',
                        'Checking save file',
                        'Reading last save file',
                        'Processing last save file',
                        'User rating OK',
                        'Computer rating OK',
                        'Games won/lost/tied OK',
                        'Games played OK',
                        'Saving new stats',
                        'Verifying file integrity',
                        'Loading fancy_exit (METHOD)',
                        'Loaded fancy_exit (METHOD)',
                        'Executing fancy_exit (METHOD)',
                        'Executed fancy_exit (METHOD)',
                        'Power off',
                    ]

logo = '''
  ___ ___  _____      _____ ___ 
 | _ \\ _ \\/ __\\ \\    / / __/ __|
 |   /  _/\\__ \\\\ \\/\\/ /| _|\\__ \\
 |_|_\\_|  |___/ \\_/\\_/ |___|___/                                
'''

def clear():
    os.system('cmd /c "cls"')
    print(logo)

def quit():
    fancy_exit()
    print(red('O'), 'Exiting rpswes...')
    time.sleep(0.001)
    exit()

def err(msg):
    print(red('??'), f'{msg}' + '\n')

def fancy_exit():
    os.system('cmd /c "cls"')

    for line in fancy_exit_lines:
        print('[' + green('+') + ']', line)
        time.sleep(0.05)

    os.system('cmd /c "cls"')