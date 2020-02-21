#!/usr/bin/python

import sys

import pprint
def rock_paper_scissors(n):
  throws = ['rock', 'paper', 'scissors']

  allPlays = [[]]
  for i in range(n):
    newPlays = []
    for play in allPlays:
      # three times  below:
      for throw in throws:
        newPlay = play + [throw]
        newPlays.append(newPlay)
    allPlays = newPlays
    
  return allPlays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')