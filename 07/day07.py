#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 7
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)

    ranked_hands = [[],[],[],[],[],[],[]]
    all_hands = [[],[],[],[],[],[],[]]
    for ln in lns:
        temp_hand = tuple(ln.split())
        hand = (hand_fixer(temp_hand[0]),temp_hand[1])
        type = hand_checker(hand)
        all_hands[type].append(hand)

    for i, rank in enumerate(all_hands):
        for j, hand in enumerate(rank):
            ranked_hands[i] = hand_sort(hand, ranked_hands[i])
    
    winnings = 0
    i = 1
    for type in ranked_hands:
        for hand in type:
            winnings += i * int(hand[1])
            i+=1
    

    return winnings

def hand_sort(hand, ranked_hands):
    for i,check_hand in enumerate(ranked_hands):
        if int(hand[0],16) < int(check_hand[0],16):
            ranked_hands.insert(i, hand)
            return ranked_hands

    
    ranked_hands.append(hand)
    return ranked_hands

def p2(v):
    lns = get_lines(v)

    ranked_hands = [[],[],[],[],[],[],[]]
    all_hands = [[],[],[],[],[],[],[]]
    for ln in lns:
        temp_hand = tuple(ln.split())
        hand = (hand_fixer(temp_hand[0]),temp_hand[1])
        if hand[0].find('b') > -1:
            type = 0
            for i in range(2,15):
                if i != 11:
                    joker_hand = (hand[0].replace('b', hex(i)[2]), hand[1])
                    joker_type = hand_checker(joker_hand)
                    if joker_type > type:
                        type = joker_type
            hand = (hand[0].replace('b',str(1)), hand[1])
            all_hands[type].append(hand)
        else:
            type = hand_checker(hand)
            all_hands[type].append(hand)
        
    for i, rank in enumerate(all_hands):
        for j, hand in enumerate(rank):
            ranked_hands[i] = hand_sort(hand, ranked_hands[i])
    
    winnings = 0
    i = 1
    for j,type in enumerate(ranked_hands):
        for hand in type:
            winnings += i * int(hand[1])
            i+=1
    

    return winnings

def hand_fixer(hand):
    hand = hand.replace('T', 'a')
    hand = hand.replace('J', 'b')
    hand = hand.replace('Q', 'c')
    hand = hand.replace('K', 'd')
    hand = hand.replace('A', 'e')
    return hand

def hand_checker(hand):

    #sort the hand to make finding the type of hand easier
    sorted_hand = sort_hand(hand[0])
    
    for i,c in enumerate(sorted_hand):

        matched_cards = re.findall(c, sorted_hand)
        unmatched_cards = re.sub(c, '', sorted_hand)
        cards = len(matched_cards)

        #check for 5 of a kind and rank it
        if cards == 5: #five of a kind
            return 6
        elif cards == 4: #four of a kind
            return 5
        elif cards >= 2: #three of a kind, fullhouse, two pair, or one pair
            if cards == 3: #three of a kind or fullhouse
                if unmatched_cards[0] == unmatched_cards[1]: #fullhouse
                    return 4
                else:
                    return 3
            else: #two pair or one pair or a fullhouse wiht a 2/3 combo
                #loop through remaining two.....to look for another pair
                if unmatched_cards[0] == unmatched_cards[1]:
                    if unmatched_cards[1] == unmatched_cards[2]: #fullhouse
                        return 4
                    else:
                        return 2
                if unmatched_cards[1] == unmatched_cards[2]:
                    return 2
                else: #only a pair
                    return 1
                
        elif i == 4: #high card
            #hand_value = int(hand,16)
            return 0
        else:
            True


    return

def sort_hand(str):
    return ''.join(sorted(str))

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
    #cmds = ['run2']
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
