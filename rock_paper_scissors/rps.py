#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    outcomes = []

    def find_outcome(n, result=[]):
        # base case
        if n == 0:
            outcomes.append(result)
            return
        # move towards the base case
        for play in plays:
            find_outcome(n - 1, result + [play])

    # call the find_outcome helper function
    find_outcome(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
