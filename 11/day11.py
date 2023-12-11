#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2023

import numpy as np
import itertools as iter

def p1(v):
    lns = get_lines(v)
    time1 = time.perf_counter()
    universe = np.asarray([[*ln] for ln in lns])
    empty_rows = np.all(universe == '.', axis=1)
    empty_cols = np.all(universe == '.', axis=0)

    galaxies = np.transpose((universe=='#').nonzero())
    galaxy_pairs = iter.combinations(galaxies,2)

    p1_ans = 0
    p2_ans = 0

    scalar = 1000000

    for pair in galaxy_pairs:
        y1, x1 = pair[0]
        y2, x2 = pair[1]

        x1, x2 = sorted([x1,x2])
        y1, y2 = sorted([y1,y2])

        x_mult = np.count_nonzero(empty_cols[x1:x2] == True)
        y_mult = np.count_nonzero(empty_rows[y1:y2] == True) 

        x_len = abs(x2 - x1)
        y_len = abs(y2 - y1)

        dist = x_len + y_len + x_mult + y_mult
        dist_2 = x_len + y_len + (x_mult + y_mult) * (scalar - 1)

        p1_ans += dist
        p2_ans += dist_2
    
    time2 = time.perf_counter()
    print('time: ' + str(time2 - time1))
    print('p1: ' + str(p1_ans))
    print('p2: ' + str(p2_ans))
    return True

def p2(v):
    return p1(v)

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
    print('Commands:', cmds)
    #cmds = ['run_samples','samples_only', 'run1']
    cmds = ['run1']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
