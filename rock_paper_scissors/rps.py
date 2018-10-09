#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  import itertools
  result = []
  for combos in itertools.product(["rock", "paper", "scissors"], repeat=n):
    result.append(list(combos))
  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')