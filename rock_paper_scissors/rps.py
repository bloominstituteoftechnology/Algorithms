#!/usr/bin/python

import sys
import math
import itertools

def rock_paper_scissors(n):
  if n < 1:
    return [[]]
  obj = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
  }
  ret = []

  tup = list(itertools.product('rps', repeat=n))
  
  for el in tup:
    ret.append(list(el))

  ret = [[obj[x] for x in row] for row in ret]
  return ret


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')