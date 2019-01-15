#!/usr/bin/python

import sys

type = ['rock', 'paper', 'scissors']
def rock_paper_scissors(n):
  return game_helper(n, new =[])

def game_helper(n, new):
  if n == 0:
    new.append([])
  else:
    new[n] += game_helper(n-1, ) + game_helper

  return new
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

## can't have the same list in the main list (matching plays)
## 