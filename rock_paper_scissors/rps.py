#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    rps = ['rock', 'paper', 'scissors']
    selected = []

    def loop(n, plays):

        nonlocal rps, selected

        if n < 0:
            plays.append(selected)
            return None

        for selector in range(3):
            selected.append(rps[selector])
            loop(n - 1, plays)

            selected = selected[:-1]

        return plays

    if n == 0:
        return [[]]
    else:
        return loop(n - 1, [])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
