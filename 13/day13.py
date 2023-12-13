#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 13
def get_year(): return 2023

import numpy as np
import math

def p1(v):
    time1 = time.perf_counter()
    chunks = v.split('\n\n')
    ans = 0
    ans2 = 0
    for chunk in chunks:
        lns = chunk.splitlines()
        pattern = np.asarray([[*ln] for ln in lns])

        v1, v2 = mirror_finder(pattern)

        ans += v1
        ans2 += v2

    time2 = time.perf_counter()

    print('time: ' + str(time2 - time1))
    
    print(str(ans))
    print(str(ans2))
    return ans

def p2(v):
    return p1(v)


def mirror_finder(pattern):

    value = refl_line(pattern, 100, False)
    new_value = refl_line(pattern, 100, True)

    if value == 0:
        value = refl_line(np.rot90(pattern, -1), 1, False)

    if new_value == 0:
        new_value = refl_line(np.rot90(pattern, -1), 1, True)

    return value, new_value

def refl_line(pattern, multiplier, dirty_mirror):
    arr_size = len(pattern) - len(pattern) % 2

    for i in range(arr_size):

        lwr = max(0, 2 * i + 1 - arr_size )

        sliced_array = pattern[lwr: 2 * (i + 1)]
        
        mid = int(len(sliced_array)/2)
        slice1 = sliced_array[:mid]
        slice2 = sliced_array[mid:][::-1]

        if dirty_mirror:
            if smudgey(slice1, slice2):
                return multiplier * (lwr + mid)
        else:
            if np.array_equal(slice1,slice2):
                return multiplier * (lwr + mid)
            
    return 0


def smudgey(slice1, slice2):
    diffs = 0
    for x, row in enumerate(slice1):
        for y, col in enumerate(row):
            if col != slice2[x][y]:
                diffs += 1
            if diffs > 1:
                return False
    
    if diffs == 1:
        return True
    
    return False

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
    #cmds = ['samples_only','run_samples','run1']
    cmds = ['run1']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
