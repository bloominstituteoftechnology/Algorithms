#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #holds potential plays
  rps = ["rock", "paper", "scissors"]
  #holds results
  result = []

  def helper(action, playsLeft):
    #base case for 0
    if playsLeft == 0:
      return result.append(action)
    else:
      #for each potential play, pass the list and the current play n times
      for play in rps:
        helper([*action, play], playsLeft - 1)

  helper([], n)
  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')