#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  possibleOutcomes = []

  # if n == 1:
  #   print(rps)
  # if n >= 2: 
  #   for i in rps:
  #     possibleOutcome.append(rps[i] )
        


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')