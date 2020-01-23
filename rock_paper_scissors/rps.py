#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options=['rock','paper','scissors']
  outcome=[]

  def helper (n, result):
    if n==0:
      outcome.append(result)
    else:
      for x in options:
        helper(n-1, result+[x])
  helper(n,[])
  return outcome





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')