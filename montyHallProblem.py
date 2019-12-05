#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import argparse
import random
from itertools import permutations
from math import floor

""" Compute a solution to the Monty Hall problem

This script computes a the probabilty to win at Let's Make a Deal game show
switching doors when the host asks you if you want to do so.
"""

def montyHallProcess(N):
    # Init the variable
    i = 0 # counter
    keep = 0 # you keep the selected door
    change = 0 # you change the selected door

    # We generate every possibility
    gifts = [1, 0, 0]; # 1 : win && 0 : loose
    doorsPermutations = list(permutations(gifts))
    selectedPermutation = list(random.choice(doorsPermutations))

    while i < N:
        i+=1

        #Selection of a door in the selected possibility
        doorIndexSelected = random.randint(0, len(selectedPermutation)-1)
        doorSelected = selectedPermutation[doorIndexSelected]

        # If we choose the right door, we should keep it
        if doorSelected == 1:
            keep += 1 / N
        else:
            change += 1 / N

    print("Probability to win if we switch doors: {}".format(change))
    print("Probability to win if we keep the one we choose : {}".format(keep))

    ratio = floor(change / keep)

    if (ratio > 1) :
        compare = "higher"
    elif (ratio < 1):
        compare = "smaller"
    else:
        compare = "equal"
    print("By the way, your chance to win by switching are {} {} than keeping your choice".format(int(change/keep), compare))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute a solution to the Monty Hall problem.')
    parser.add_argument('iteration', help='''Number of iteration to compute the 
                        solution. Default is 100,000''', nargs='?', 
                        default=100000, type=int)
    args = parser.parse_args()
    montyHallProcess(args.iteration)
