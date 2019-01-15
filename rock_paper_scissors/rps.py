#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # PR(n,r) = n^r
  if n == 0:
    return 0
  if n == 1:
    return 3
  if n == 2:
    return 9
  if n == 3:
    return 27
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')