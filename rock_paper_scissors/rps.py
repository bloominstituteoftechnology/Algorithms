#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #start with a list of choice
  choices=['rock','paper','scissors']
  psb=[]
  def permu (which_round, result):
    if which_round==0:
      psb.append(result)
    else:
      for choice in choices:
        permu(which_round-1, result+[choice])
  permu(n,[])
  return psb

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')