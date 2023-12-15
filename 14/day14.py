#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 14
def get_year(): return 2023

import numpy as np
import functools


def p1(v):
    lns = get_lines(v)
    #chunks = v.split('\n\n')
    ans = 0

    rocks = np.asarray([[*ln] for ln in lns])
    rocks = np.rot90(rocks, 1)

    rocks, ans = tilt_mirror(rocks)

    return ans

def p2(v):
    time1 = time.perf_counter()
    lns = get_lines(v)
    ans = 0

    rocks = np.asarray([[*ln] for ln in lns])
    rocks = np.rot90(rocks, 1)

    spins = 1000
    for i in range(spins):
        for j in range(4):
            rocks, ans = tilt_mirror(rocks)
            rocks = np.rot90(rocks, -1)

        weight = 0
        #calculate north wall load
        for r in rocks:
            for n, rock in enumerate(r):
                if rock == 'O':
                    weight += len(r) - n

        print('spin: ' + str(i+1) + ' load: ' +  str(weight)) 
        
    time2 = time.perf_counter()
    print('time: ' + str(time2 - time1))
    return ans

def tilt_mirror(rocks):
    
    #do matrix rotation for each tilt....
    weight = 0
    for r, row in enumerate(rocks):
        n_rocks = 0
        c_rock = 0 #cube rock spot
        new_row = []
        for c, space in enumerate(row):
            if space == '#': #cube rock
                new_row += n_rocks * ['O'] + ['.'] * (c - c_rock - n_rocks) + ['#']

                for i in range(n_rocks):
                    weight += len(row) - c_rock - i

                c_rock = c + 1
                n_rocks = 0
            elif space == 'O':
                n_rocks += 1
        new_row += n_rocks * ['O'] + ['.'] * (c - c_rock - n_rocks + 1)
        
        for i in range(n_rocks):
            weight += len(row) - c_rock - i
        rocks[r] = new_row

    return rocks, weight


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
    #cmds = ['run_samples','samples_only','run1','run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
