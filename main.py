from rps import *

logo = '''
  ___ ___  _____      _____ ___ 
 | _ \\ _ \\/ __\\ \\    / / __/ __|
 |   /  _/\\__ \\\\ \\/\\/ /| _|\\__ \\
 |_|_\\_|  |___/ \\_/\\_/ |___|___/                                
'''

print(logo)

while True:
    cmd = input('>>> ')

    if cmd == 'c':
        clear()

    elif cmd == '' or cmd == ' ':
        continue

    elif cmd == 'start' or cmd == 'x':
        run_round()

    elif cmd == 'q' or cmd == 'quit' or cmd == 'exit':
        quit()

    else:
        err(f'No command named {cmd}.')