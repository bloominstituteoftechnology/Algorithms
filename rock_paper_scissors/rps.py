#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n <= 0:
    return [[]]
    #base case 
  else:
    first_result = rock_paper_scissors(n-1)
    new_result = []
    for r in first_result:
      new_result.append(r + ["rock"])
      new_result.append(r + ["paper"])
      new_result.append(r + ["scissors"])
    return new_result  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')