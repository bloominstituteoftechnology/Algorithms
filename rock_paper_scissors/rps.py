#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #start with a list of choice
  choices=['rock','paper','scissors']
  #possible outcome will be store here
  psb=[]
  # def to determine the permutation
  def permu (which_round, result):
    #at round 0, which means no round left, append to psb
    if which_round==0:
      psb.append(result)
    else:
      # start going through choices and pick on to combine with the current index choice
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