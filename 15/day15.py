#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 15
def get_year(): return 2023

class lens:
    def __init__(self, lbl, fl=0):
        self.lbl = lbl
        self.fl = int(fl)
        self.hash = self.get_hash()
    
    def get_hash(self):
        cv = 0
        for c in self.lbl:
            cv = hash_alg(c, cv)
        return cv
    
def p1(v):
    lns = get_lines(v)
    time1 = time.perf_counter()

    hashes = lns[0].split(',')
    ans = 0
    for hash in hashes:
        cv = 0
        for c in hash:
            cv = hash_alg(c, cv)
        ans += cv
    
    time2 = time.perf_counter()
    print('p1 time: ' + str(time2 - time1))
    return ans

def p2(v):
    lns = get_lines(v)
    time1 = time.perf_counter()

    ops = lns[0].split(',')
    boxes = defaultdict(lambda: defaultdict(lens))

    for op in ops:
        opcode = op.find('=')
        if opcode > -1:  #lens definition
            l = lens(op[0:opcode], op[opcode+1:])
            boxes[l.hash][l.lbl] = l.fl
        else:           #removal operation
            l = lens(op[:-1])
            if l.lbl in boxes[l.hash]:
                del boxes[l.hash][l.lbl]
        True

    focus_power = 0
    for (box_num, box) in boxes.items():
        for i,(l,fl) in enumerate(box.items()):
            focus_power += (box_num + 1) * (i + 1) * fl
    

    time2 = time.perf_counter()
    print('p2 time: ' + str(time2 - time1))

    return focus_power

def hash_alg(c, cv):
    cv += ord(c)
    cv *= 17
    cv %= 256

    return cv

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
    #cmds=['samples_only','run_samples','run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
