#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  if n <= 0:
    return [[]]
  else:
    
    previous_results = rock_paper_scissors(n-1)
    new_results = []
    
    for result in previous_results:
      new_results.append(result + ["rock"])
      new_results.append(result + ["paper"])
      new_results.append(result + ["scissors"])
    
    return new_results


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')