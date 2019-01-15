#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possible_plays = [['rock'], ['paper'], ['scissors']]
  result = []
  if n == 0:
    return 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
