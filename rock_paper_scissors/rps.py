#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps_list = [['rock'], ['paper'], ['scissors']]

    # base case of 0
    if n == 0:
        return [[]]
    if n == 1:
        return rps_list

    # if n == 2 3^2 of options
    possible_plays = []
    for i in range(3**n):
        possible_plays.append(rps_list[i % 3])

    for i in range(len(possible_plays)):
        possible_plays[i].extend(rps_list[i % 3])

    print(possible_plays)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
