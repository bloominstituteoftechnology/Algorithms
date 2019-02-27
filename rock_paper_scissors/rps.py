#!/usr/bin/python

import sys

plays = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
    outcomes = []

    def possible_outcomes(roundsLeft, result):
      if roundsLeft == 0:
        outcomes.append(result)
        return
      for play in plays:
        possible_outcomes(roundsLeft - 1, result + [play])

    possible_outcomes(n, [])
    return outcomes
      

  

print(rock_paper_scissors(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')





















  #   # base case n = 0, return an empty array
  # if n == 0:
  #   return lst
  # # if n = 1 we return the current plays
  # if n == 1:
  #   return plays
  # # every increment of n we return the n = 1 + n = n+1
  # else:
  #   for x in range(0, n-1):
  #     lst[x].append(plays[x])
  #     n - 1
  # return lst