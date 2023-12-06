#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2023

import numpy as np

def p1(v):
    time1 = time.perf_counter()

    cards = get_lines(v)
    chunks = v.split('\n\n')

    ans = 0
    for card in cards:
        winners = card.split(':')[1].split('|')[0].strip().split()
        yours = card.split(':')[1].split('|')[1].strip().split()

        winning_array = np.isin(winners, yours)
        num_wins = np.count_nonzero(winning_array)
        if num_wins > 0:
            ans += 2 ** (num_wins - 1)

    time2 = time.perf_counter()
    return ans

def p2(v):
    cards = get_lines(v)
    chunks = v.split('\n\n')

    num_cards = np.ones(199, dtype=int)
    ans = 0

    for c, card in enumerate(cards):
        winners = card.split(':')[1].split('|')[0].strip().split()
        yours = card.split(':')[1].split('|')[1].strip().split()

        winning_array = np.isin(winners, yours)
        num_wins = np.count_nonzero(winning_array)

        for i in range(num_wins):
            num_cards[c + i + 1] += num_cards[c]
        
    ans = np.sum(num_cards)
    return ans


if __name__ == '__main__':
    cmds = get_commands()
    """
    cmds = [
        #'print_stats',
        'run1',
        #'submit1',
        #'run2',
        #'submit2',
        ]
    """
    #print('Commands:', cmds)
    #cmds = ['run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
