#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 2
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0
    bags = []

    red = 12
    green = 13
    blue = 14
    pt1 = 0
    global pt2
    pt2 = 0

    for ln in lns:
        game = ln.split(':')[0]
        rounds = ln.split(':')[1]
        round_track = []
        bags.append(round_track)

        max_red = 0
        max_blue = 0
        max_green = 0

        possible_game = True
        
        for round in rounds.split(';'):
            cubes = round.split(',')
            reveal = {}
            for cube in cubes:
                color = cube.strip().split(' ')[1]
                num = int(cube.strip().split(' ')[0])
                reveal[color] = num                

            bags[-1].append(reveal)

            if 'red' in reveal:
                max_red = max(max_red, reveal['red'])

                if reveal['red'] > red and possible_game:
                    possible_game = False 
            if 'blue' in reveal:
                max_blue = max(max_blue, reveal['blue'])

                if reveal['blue'] > blue and possible_game:
                    possible_game = False 
            if 'green' in reveal:
                max_green = max(max_green, reveal['green'])
                
                if reveal['green'] > green and possible_game:
                    possible_game = False 
        
        bag_power = max_red * max_blue * max_green
        pt2 += bag_power

        if possible_game:
            pt1 += len(bags)
        
    return pt1

def p2(v):
    return  pt2


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
    #cmds = ['run_samples','run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
