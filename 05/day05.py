#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2023

import numpy as np

def p1(v):
    time1 = time.perf_counter()
    #lns = get_lines(v)
    chunks = get_chunks(v)
    ans = 0
    map_arrays = []

    for c, chunk in enumerate(chunks):
        if c == 0:
            seeds = parse_array(chunk[0].split(), False)
            seed_pairs = []
            for i,seed in enumerate(seeds[::2]):
                seed_pairs.append([seed,seeds[2 * i - 1] + seed])

            seeds = np.sort(seeds, axis=None)
        else:
            map_arrays.append(parse_array(chunk, True))

    init_array = seeds
    p2_array = seed_pairs
    for map_array in map_arrays:
        init_array = remap_loop(init_array, map_array)
        p2_array = part2_loop(p2_array, map_array)
        p2_array = reshape(p2_array)

    ans = p2_array[0][0]
    for item in p2_array:
        ans = min(ans, item[0])

    time2 = time.perf_counter()
    print ('exec time: ' + str((time2 - time1)))
    print('part1: ' + str(min(init_array)))
    print('part2: ' +  str(ans))
    return 

def remap_loop(arr1, arr2):
    new_arr = arr1.copy()
    i = 0
    for s, seed in enumerate(arr1):
        # find seed in soil
        if seed >= arr2[0,1]:
            new_arr[s], i = remap(seed, arr2[i:])
        else:
            new_arr[s] = seed
    new_arr.sort()
    return new_arr

def remap(cond, arr1):
    for i, item in enumerate(arr1):
        if cond >= item[1] and cond < (item[1] + item[2]):
            dest = item[0] + (cond - item[1])
            return dest, i
        elif np.where(arr1 == item)[0][1] == len(arr1) - 1: 
            dest = cond
            return dest, i

def parse_array(arr, sort, sort_arg = 1):
    parsed_array = np.array([x.split() for x in arr[1:]], dtype=np.int64)

    if sort:
        parsed_array = parsed_array[parsed_array[:, sort_arg].argsort()]
    return parsed_array

def part2_loop(arr1, arr2):
    output = [] #array to hold outputs

    #arr1 will have two elements, a starting item, and a upper bound
    #arr2 will have three elements, a remap value, a starting item, and a range

    for item1 in arr1:  #go through each item in the starting array
        output.append( check_range(item1, arr2) )

    return output

def check_range(arr1, arr2):
    lb1 = arr1[0]
    ub1 = arr1[1]

    output = []

    for item2 in arr2: #go through each item in the second array    
        lb2 = item2[1]
        ub2 = lb2 + item2[2] - 1

        if lb1 < lb2 and ub1 < lb2: #both the lower and upper bound are below the first element.  this only works because we've sorted on tthe order
            return [lb1, ub1]

        if lb1 < lb2 and ub1 >= lb2: #the lower bound is below the first element, but the upper bound intersects.  this requires a split of the data
            output.append([lb1, lb2 - 1])
            output.append( check_range([lb2, ub2], arr2) )
            return output
        
        if lb1 >= lb2 and ub1 <= ub2:
            offset = lb2 - item2[0]
            return [lb1 - offset, ub1 - offset]

        if lb1 >= lb2 and lb1 < ub2 and ub1 > ub2:
            offset = lb2 - item2[0]
            output.append([lb1 - offset, ub2 - offset])
            output.append( check_range([ub2 + 1, ub1], arr2))
            return output
    
    #if we've gotten here, no returns have happened, meaning everything is above every other value in the list, so just return the original bounds
    return [lb1, ub1]
        
def reshape(arr):
    output = []
    flat_list = flatten(arr)

    for i,s in enumerate(flat_list[::2]):
        output.append([s,flat_list[2 * i + 1] ])
    return output

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def p2(v):
    return


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
    cmds = [ 'run1']
    print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
