#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps_list = [['rock'], ['paper'], ['scissors']]

    # base case of 0
    if n == 0:
        return []
    if n == 1:
        return rps_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
