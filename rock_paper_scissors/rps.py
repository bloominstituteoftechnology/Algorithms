#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # initialize stuff
    plays = ['rock', 'paper', 'scissors']

    def rec_rps(outcomes, n):
        # base case
        if n == 0:
            return [[]]
        # recursive case
        else:
            outcomes = rec_rps(outcomes, n-1)
            new_outcomes = []
            for p in plays:
                for o in outcomes:
                    new_outcomes.append(o+[p])
            return new_outcomes

    return rec_rps([], n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
