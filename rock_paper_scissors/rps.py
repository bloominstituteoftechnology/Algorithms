#!/usr/bin/python

import sys
from itertools import product

def rock_paper_scissors(n):
  print(n)
  array = ['rock', 'paper', 'scissors']
  if n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    # print(f'This is the list === {list(product(array, repeat = n))}') #returns a tuple
    combinations = [list(x) for x in list(product(array, repeat = n))]
    return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')