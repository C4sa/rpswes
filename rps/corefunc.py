import os
from rps.color import *

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
    exit()

def err(msg):
    print(red('??'), f'{msg}' + '\n')