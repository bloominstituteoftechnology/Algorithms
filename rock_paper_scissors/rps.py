#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    allpos = []

    def rec(i, item, clist=[]):
        print('here', item, clist)
        if i == 0:
            return clist
        else:
            clist = clist + [item]
            allpos = [[rec(i-1, 'rock', clist)] + [rec(i-1, 'paper', clist)]]

    rec(n, 'rock')
    print('paper')
    rec(n, 'paper')
    return allpos


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
