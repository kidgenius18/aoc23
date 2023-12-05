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
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    for c, chunk in enumerate(chunks):
        if c == 0:
            seeds = parse_array(chunk[0].split(), False)
            seeds = np.sort(seeds, axis=None)
        elif c == 1:
            seed_to_soil = parse_array(chunk, True)
        elif c == 2:
            soil_to_fertilizer = parse_array(chunk, True)
        elif c == 3:
            fertilizer_to_water = parse_array(chunk, True)
        elif c == 4:
            water_to_light = parse_array(chunk, True)
        elif c == 5:
            light_to_temperature = parse_array(chunk, True)
        elif c == 6:
            temperature_to_humidity = parse_array(chunk, True)
        elif c == 7:
            humidity_to_location = parse_array(chunk, True)

    #loop through each seed
    dest = remap_loop(seeds, seed_to_soil)
    dest = remap_loop(dest, soil_to_fertilizer)
    dest = remap_loop(dest, fertilizer_to_water)
    dest = remap_loop(dest, water_to_light)
    dest = remap_loop(dest, light_to_temperature)
    dest = remap_loop(dest, temperature_to_humidity)
    dest = remap_loop(dest, humidity_to_location)

    time2 = time.perf_counter()
    print ('exec time: ' + str((int(time2) - int(time1))))
    return min(dest)

def remap_loop(arr1, arr2):
    new_arr = arr1.copy()
    i = 0
    for s, seed in enumerate(arr1):
        # find seed in soil
        if seed >= arr2[0,1]:
            new_arr[s], i = remap(seed, arr2[i:])
        else:
            new_arr[s] = seed
    print(new_arr)
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
    parsed_array = np.array([x.split() for x in arr[1:]], dtype=int)

    if sort:
        parsed_array = parsed_array[parsed_array[:, sort_arg].argsort()]
    return parsed_array

def part2_loop(arr1, arr2):
    
    
    new_arr = []
    for item1 in arr1:
        l_bound = item1[1]
        u_bound = l_bound + item1[2]
        
        for item in arr2:
            if item[0] >= l_bound and item[0] < u_bound:
                new_arr.append(item)

    new_arr = new_arr[new_arr[:, 0].argsort()]
    return new_arr


def p2(v):
    time1 = time.perf_counter()
    #lns = get_lines(v)
    chunks = get_chunks(v)
    ans = 0
    seeds = set()
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    for c, chunk in enumerate(chunks):
        if c == 0:
            seed_pairs = parse_array(chunk[0].split(), False)
        elif c == 1:
            seed_to_soil = parse_array(chunk, True, 0)
        elif c == 2:
            soil_to_fertilizer = parse_array(chunk, True, 0)
        elif c == 3:
            fertilizer_to_water = parse_array(chunk, True, 0)
        elif c == 4:
            water_to_light = parse_array(chunk, True, 0)
        elif c == 5:
            light_to_temperature = parse_array(chunk, True, 0)
        elif c == 6:
            temperature_to_humidity = parse_array(chunk, True, 0)
        elif c == 7:
            humidity_to_location = parse_array(chunk, True, 0)

    #go backwards since we know the lowest output has to be in the lowest range of the final array.  then drive backwards into the initial array/range
    #humidity_to_location = humidity_to_location[humidity_to_location[:, 0].argsort()]
    dest = part2_loop(humidity_to_location, temperature_to_humidity)
    dest = part2_loop(dest, light_to_temperature)
    dest = part2_loop(dest, water_to_light)
    dest = part2_loop(dest, fertilizer_to_water)
    dest = part2_loop(dest, soil_to_fertilizer)
    dest = part2_loop(dest, seed_to_soil)

    time2 = time.perf_counter()
    print ('exec time: ' + str((int(time2) - int(time1))))
    return min(dest)


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
    cmds = [ 'run2']
    print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
