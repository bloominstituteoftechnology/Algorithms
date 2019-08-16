#!/usr/bin/python

import itertools
import sys


def rock_paper_scissors(n):
    plays = ["rock", "paper", "scissors"]
    combo = [list(c) for c in itertools.permutations(plays, n)]
    new_combo = []

    for i in combo:
        new_combo.append(i)
    return new_combo

print(rock_paper_scissors(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
