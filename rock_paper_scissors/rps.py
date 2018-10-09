#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = [["rock"], ["paper"], ["scissors"]]
  if n == 0:
    return [[]]
  if n == 1:
    return options

  print( [options[1]] * n + options[[2]] * n + options[[3]] * n )

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')