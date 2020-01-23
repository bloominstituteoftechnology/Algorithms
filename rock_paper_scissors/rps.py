#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']

  for option in options:
    for count in range(1,n + 1):
      



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')