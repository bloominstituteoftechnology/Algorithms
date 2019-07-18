#!/usr/bin/python

import sys
from itertools import combinations_with_replacement

def rock_paper_scissors(n):
    possibilities = ['rock', 'paper', 'scissors']
    return [[*i] for i in list(combinations_with_replacement(possibilities, n))]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
