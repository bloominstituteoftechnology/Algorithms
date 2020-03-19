#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #start
  choices =  ['rock', 'paper', 'scissors']
  possible_plays = []

  #base 
  def rps_helper_fun(result, num_plays):
        # this should stop the recursion if there are no plays
    if num_plays == 0:
      possible_plays.append(result)
      return
    for i in range(0, len(choices)):
      rps_helper_fun(result + [choices[i]], num_plays -1)
  rps_helper_fun([], n)
  return possible_plays

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')