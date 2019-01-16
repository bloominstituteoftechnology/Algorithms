#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    string = [['rock'], ['paper'], ['scissors']]
    for x in string:
      



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')


#### Enter number of rps games. Print the first position that man times. 