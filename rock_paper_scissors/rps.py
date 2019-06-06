#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    rps = ['rock', 'paper', 'scissors']
    selected = []

    def loop(n, plays):

        nonlocal rps, selected

        # print(locals())
        if n < 0:
            plays.append(selected)
            return None

        for rotate in range(3):
            for selector in range(3):
                selected.append(rps[selector])
                print('selected:', selected)
                loop(n - 1, plays)

                selected = selected[:-1]

            rps = rps[1:] + [rps[0]]

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
