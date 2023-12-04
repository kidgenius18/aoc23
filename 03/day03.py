#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2023

import re

def p1(v):
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0
    gear_ratio = 0
    symbols = []
    for i, ln in enumerate(lns):
        symbols.append(list(range(len(ln)))) #create an object to hold all symbol positions

        #find everything which isnt a symbol.  could do a regex of all symbols, but better to use what we know is not a symbol, _
        #  instead of hardcoding in all symbols
        parts = re.finditer('[0-9\.]', ln)         
        
        for part in parts:
            symbols[i].remove(part.start()) #remove all parts
        
        #all symbol locations left, iterate on all existing symbol locations
        if symbols[i]:
            for pos in symbols[i]:
                gears = []
                
                start_ln = -1
                if i == 0:
                    start_ln = 0
               
                end_ln = 2
                if i == len(symbols):
                    end_ln = 1
                
                for x in range(start_ln, end_ln):

                    if i == 10:
                        print(i)
                    part_nums = look_around(lns[i + x], pos)
                
                    for item in part_nums:
                        if item.isdigit():
                            gears.append(int(item))
                            ans += int(item)
                
                if len(gears) == 2:
                    gear_ratio += gears[0] * gears[1]

    print ('gear ratio = ' + str(gear_ratio))
    return ans

def look_around(ln, pos):

    index = []
    for dir in [-1,1]:
        idx = dir
        try:
            while ln[pos + idx].isdigit():
                idx += dir
        except:
            idx = idx
        
        index.append(pos + idx)
    
    if ln[pos].isdigit():
        separator = ' '
    else:
        separator = ln[pos] 

    index[0] = max(0, index[0] + 1)
    return ln[index[0] : index[1]].split(separator)

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
    cmds=['run_samples','samples_only','run1']
    #cmd = ['run1']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
