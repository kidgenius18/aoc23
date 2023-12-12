#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2023

import re
import functools

def p1(v):
    time1 = time.perf_counter()
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        sequence, springs = ln.split()
        springs = springs.split(',')

        spring_seq = '.'
        for s in springs:
            #take each spring size and turn it into a block of #'s, with a single period between them.
            spring_seq += '#' * int(s) + '.'
        
        ans += recurser(sequence, spring_seq)
        
    time2 = time.perf_counter()
    print('time: ' + str(time2 - time1))
    return ans

def p2(v):
    time1 = time.perf_counter()
    lns = get_lines(v)
    ans = 0
    for i, ln in enumerate(lns):
        sequence, springs = ln.split()
        springs = springs.split(',')
        springs = springs * 5

        sequence = ((sequence + '?') * 5)[:-1]

        spring_seq = '.'
        for s in springs:
            #take each spring size and turn it into a block of #'s, with a single period between them.
            spring_seq += '#' * int(s) + '.'

        ans += recurser(sequence, spring_seq)
    

    time2 = time.perf_counter()
    print('time: ' + str(time2 - time1))

    return ans

@functools.cache
def recurser(pattern, spring):
    argt = 0
    
    per_pattern = pattern.replace('?','.',1)
    ht_pattern = pattern.replace('?', '#', 1)

    #try replacing the ? with a '.', and then with a '#', to see if it matches our sequence
    argt += finder(per_pattern, spring)
    argt += finder(ht_pattern, spring)

    return argt

def finder(pattern, spring):
    #add a leading/trailing '.' character so everything aligns with the input check
    pattern = '.' + pattern + '.'
    #replace all multiple periods with single periods.  we dont care how many periods are between each spring
    #the set of springs at the beginning was converted to #'s with a single period between each.  
    #this regex will replicate the input group
    pattern = re.sub('\.+','.',pattern)
    #find where the first '?' is located.
    slicer = pattern.find('?')

    #if the pattern of .'s and #'s up to the current ? char matches, then this is a potentially matching sequence.
    #if we dont match up at this point, there is no point in continuing on as this wont be match.
    #we can just return and move on to the next seq
    if pattern[:slicer] == spring[:slicer]:
        #if no more ? exist, then this is a full seq which matches
        if pattern.find('?') == -1:
            return 1
        else:
            #if there still exists a ?, then we continue the substitution.thi
            return recurser(pattern, spring)
    
    return 0

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
    #cmds = ['samples_only','run_samples','run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
