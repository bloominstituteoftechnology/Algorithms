#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    outcomes = []
    for play in rock_paper_scissors(n - 1):
      outcomes = outcomes + [play + ['rock'], play + ['paper'], play + ['scissors']]
    return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')