#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    combos = []
    plays = ['rock', 'paper', 'scissors']

    def battle(n, combo=[]):
        if n == 0:
            combos.append(combo)
            return
        for play in plays:
            battle(n - 1, combo + [play])
    battle(n, [])
    return combos


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
