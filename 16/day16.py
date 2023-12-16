#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 16
def get_year(): return 2023

import numpy as np

class beam:
    def __init__(self, pos, dir, visited, loop = False):
        self.pos = pos
        self.dir = dir
        self.visited = visited
        self.loop = loop

    def new_pos(self, yx, cave): #passhtrough function
        self.pos = tuple(yx)
        
        self.wall(cave)

    def wall(self, cave):
        #handle the case of being on an edge.....
        #probably can be more elegant here
        max_y = len(cave)
        max_x = len(cave[0])
        if self.pos[0] + self.dir[0] < 0:
            self.dir[0] = 0
        elif self.pos[0] + self.dir[0] >= max_y:
            self.dir[0] = 0
        if self.pos[1] + self.dir[1] < 0:
            self.dir[1] = 0
        elif self.pos[0] + self.dir[0] >= max_x: #would need to modify this if its not a square cave/input
            self.dir[1] = 0
        
        True


def p1(v):
    lns = get_lines(v)
    cave = np.asarray([[*ln] for ln in lns])

    beams = [beam([0,-1],[0,1])]

    ans = bounce_all(cave, beams)

    return ans

def p2(v):
    lns = get_lines(v)
    cave = np.asarray([[*ln] for ln in lns])

    time1 = time.perf_counter()
    max_energy = 0
    for i in range(len(cave)): #follow the vertical walls
        beams = [beam([i,-1],[0,1],defaultdict())]
        e_level = bounce_all(cave, beams)
        max_energy = max(max_energy, e_level)
        
        beams = [beam([i,len(cave[i])], [0,-1],defaultdict())]
        e_level = bounce_all(cave, beams)
        max_energy = max(max_energy, e_level)

        time2 = time.perf_counter()   
        if i % 10 == 0:
            print('iter: ' + str(i) + ' , time: ' + str(time2-time1))
            time1 = time.perf_counter()
    
    for j in range(len(cave[0])): #follow the horizontal walls
        beams = [beam([-1,j],[1,0],defaultdict())]
        e_level = bounce_all(cave, beams)
        max_energy = max(max_energy, e_level)
        
        beams = [beam([len(cave[i]),j], [-1, 0],defaultdict())]
        e_level = bounce_all(cave, beams)
        max_energy = max(max_energy, e_level)

        time2 = time.perf_counter()   
        if j % 10 == 0:
            print('iter: ' + str(j) + ' , time: ' + str(time2-time1))
            time1 = time.perf_counter()

    return max_energy

def bounce_all(cave, beams):
    energized = {(0,0)}

    while True:
        beams, visited = bounce(cave, beams)
        
        [energized.add(e) for e in visited]
        if len(beams) == 0:
            return len(energized)
    
    return
        
def bounce(cave, beams):
    #cave is the array of all locations
    #beams is an array holding numerous light beams
    #   - each beam has a current location and a direction
    #   - direction is an array, of x any y.
    #       -  [0,-1] indicates a left traveling beam
    #       -  [1,0] indicates an downward traveling beam
    c_min = [0,0]
    c_max = [len(cave) - 1, len(cave[0]) - 1]     

    new_beams = []
    energized = set()
    for b in beams:
        #if b.pos[0] == 7 and b.pos[1] == 5:
        #    True
        if np.any(np.equal(np.abs(b.dir),1)): #only do a computation if the beam has velocity    
            yx = np.add(b.pos, b.dir)
            yx = yx.clip(min=c_min, max=c_max)
            
            sq = cave[yx[0],yx[1]]

            if sq == '-' or sq == '|':
                if (b.dir[0] == 0 and sq == '-') or (b.dir[1] == 0 and sq == '|'): #perform pass-through
                    b.new_pos(yx, cave)
                    
                else: #perform a split
                    b, new_beam = split(b, yx, cave)
                    new_beams.append(new_beam)

            elif sq == '/':
                b.dir = np.flip(b.dir) * -1
                b.new_pos(yx, cave)

            elif sq == '\\':
                b.dir = np.flip(b.dir)
                b.new_pos(yx, cave)

            else: # '.'
                b.new_pos(yx, cave)

            energized.add((b.pos[0], b.pos[1]))
        
        if b.pos in b.visited: #check if space has been visited
            if b.visited[b.pos] == tuple(b.dir): #check if the direction is the same
                #if so, then we are in a loop and should no longer include this beam
                b.loop = True
            else:
                b.visited[b.pos] = tuple(b.dir)
        else:
            b.visited[b.pos] = tuple(b.dir)

        if not b.loop and tuple(b.dir) != (0,0):
            new_beams.append(b)
    
    return new_beams.copy(), energized

def split(b, yx, cave):
    b.new_pos(yx, cave)
    b.dir = np.flip(b.dir)
    newbeam = beam(b.pos, b.dir * -1,b.visited)
    
    return b, newbeam
       
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
    cmds = ['run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
