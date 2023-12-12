#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        springs, groups = ln.split()
        #spring_counts = springs.split(',')
        groups = groups.split(',')
        
        spring_chars = len(springs)
        spring_pattern = [None] * 2**spring_chars #populate with the current pattern...
        
        pattern_counter = 0
        for i, sp in enumerate(springs):
            if sp == '?':
                slice_idx = 2 ** pattern_counter
                loc_idx = i+1

                if pattern_counter == 0:
                    spring_pattern[0:1] = [springs, springs]
                else:                
                    spring_pattern[slice_idx : slice_idx * 2] = spring_pattern[0 : slice_idx]

                pattern_counter += 1
                
                for sp_idx in range(slice_idx):
                    spp = spring_pattern[sp_idx]

                    spring_pattern[sp_idx] = spp[:loc_idx].replace('?','.') + spp[loc_idx:]
                    spring_pattern[sp_idx + slice_idx] = spp[:loc_idx].replace('?','#')+ spp[loc_idx:]
            #ans += 1
        
        arrangements = 0
        for i in range(slice_idx * 2):
            
            spring_pattern[i] = '.' + spring_pattern[i] + '.'
            ßßß
            finder = 0 
            #debug_spring = spring_pattern[i]

            for g in groups:
                spring = '.' + '#' * int(g) + '.'
                spring_loc = spring_pattern[i].find(spring)


                if spring_loc > -1 and spring_pattern[i].find('#') - 1 == spring_loc:
                    finder += 1
                spring_pattern[i] = spring_pattern[i].replace(spring, '.', 1)
                
    
            if all([x == '.' for x in spring_pattern[i]]) and finder == len(groups):
                arrangements += 1


        #print ('arrangements: ' + str(arrangements))
    
        ans += arrangements
    return ans

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
    #cmds = ['samples_only','run_samples','run1']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
