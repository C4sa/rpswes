from rps.color import *
from rps.corefunc import *

def get_stats(rating_p, rating_c, hr_p, hr_c, won, lost, tied, played, title):
    wl_ratio = int(won) - int(lost)

    print('-- STATS --\n')

    print(green(f'{won} GAMES WON'))
    print(yellow(f'{tied} GAMES TIED'))
    print(red(f'{lost} GAMES LOST\n'))

    print(f'GAMES PLAYED: {played}')
    if wl_ratio == 0: print('RAW WIN/LOSS RATIO:', gray(str(wl_ratio)), '\n')
    if wl_ratio > 0: print('RAW WIN/LOSS RATIO:', green('+' + str(wl_ratio)), '\n')
    if wl_ratio < 0: print('RAW WIN/LOSS RATIO:', red(str(wl_ratio)), '\n')

    if rating_p < 500: print(gray(f'YOUR RATING: {rating_p}'))
    if rating_p >= 500 and rating_p < 1000: print(green(f'YOUR RATING: {rating_p}'))
    if rating_p >= 1000 and rating_p < 1500: print(cyan(f'YOUR RATING: {rating_p}'))
    if rating_p >= 1500 and rating_p < 2000: print(yellow(f'YOUR RATING: {rating_p}'))
    if rating_p >= 2000 and rating_p < 3000: print(magenta(f'YOUR RATING: {rating_p}'))
    if rating_p >= 3000 and rating_p < 5000: print(blue(f'YOUR RATING: {rating_p}'))
    if rating_p >= 5000 and rating_p < 10000: print(red(f'YOUR RATING: {rating_p}'))
    if rating_p >= 10000: print(red(f'YOUR RATING: {rating_p} ULTRA MEGA GIGA INTERNATIONAL GRAND DRAGON MASTER SLAYER [UMGIGDMS]'))    

    if rating_c < 500: print(gray(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 500 and rating_c < 1000: print(green(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 1000 and rating_c < 1500: print(cyan(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 1500 and rating_c < 2000: print(yellow(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 2000 and rating_c < 3000: print(magenta(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 3000 and rating_c < 5000: print(blue(f'COMPUTER RATING: {rating_c}'))
    if rating_c >= 5000: print(red(f'COMPUTER RATING: {rating_c} ULTRA MEGA GIGA INTERNATIONAL GRAND DRAGON MASTER SLAYER [UMGIGDMS]\n'))

    print('\nYOUR TITLE: ', end = '')
    if title == '': print(gray('You don\'t have a title yet! The first one you can get is\ncalled [NM] New Master, and you can get it by reaching a peak rating of 2200 and typing the \'nm\' command!\nYou can learn more on the wiki: https://github.com/C4sa/rpswes/wiki'))
    if title == 'nm': print(green('[NM] New Master'))
    if title == 'lm': print(cyan('[LM] Local Master'))
    if title == 'cm': print(magenta('[CM] Casual Master'))
    if title == 'gm': print(red('[GM] Grandmaster\n') + gray('Congratulations on your journey in rpswes and getting this far!'))

    print('\nHIGHEST RATING (YOU): ' + yellow(str(hr_p)))
    print('HIGHEST RATING (COMPUTER): ' + yellow(str(hr_c)))

    input('\n<< Back [ENTER]\n')
    clear()

def add(stat, value):
    output = stat + value
    return output

def remove(stat, value):
    output = stat - value
    return output