#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  map_dict = {0: 'rock', 1: 'paper', 2: 'scissors'}
  out = []
  for i in range(3**n):
    temp = []
    for j in range(n):
      temp.insert(0, map_dict[(i // 3 ** j) % 3])
    out.append(temp)
  return out

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')