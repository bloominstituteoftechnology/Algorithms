#!/usr/bin/python

import sys
from itertools import product  
def rock_paper_scissors(n):
  results = product(["rock", "paper", "scissors"], repeat = int(n))
  formated_result = [list(n) for n in list(results)]
  return list(formated_result)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')