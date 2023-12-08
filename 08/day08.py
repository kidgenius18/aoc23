#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 8
def get_year(): return 2023
import numpy as np


def p1(v):
    sys.setrecursionlimit(30000)
    dirs, chunks = v.split('\n\n')
    lns = get_lines(chunks)
    lcm = 1
    nodes = {}
    for ln in lns:
        node_key, node_tup = ln.split(' = ')
        t1, t2 = node_tup.split(', ')
        nodes[node_key] = (t1[1:], t2[:-1])
    
    node_steps = {}

    time1 = time.perf_counter()
    for node in nodes:
        if node[-1:] == 'A':
            node_steps[node] = walk_map(dirs, nodes, node)

    for node in node_steps:
        lcm = np.lcm(lcm, node_steps[node])

    time2 = time.perf_counter()

    print('part1: ' + str( node_steps['AAA']))
    print('part2: ' + str(lcm))
    print('time: ' + str(time2-time1))
    return lcm

def walk_map(dirs, nodes, node):
    map_dir = {"L": 0, "R": 1}
   
    dir = map_dir[dirs[0]]
    dirs = dirs[1:] + dirs[0]
    next_node = nodes[node][dir]

    step = 1
    if next_node[-1:] == 'Z':
        return step
    
    step += walk_map(dirs, nodes, next_node)

    return step


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
    cmds = ['run1']
    print('Commands:', cmds)
    main(get_year(), get_day(), p1, '', cmds, FILE=__file__)
