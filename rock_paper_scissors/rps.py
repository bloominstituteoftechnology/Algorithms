#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  outcomes = []

  def find_outcome(n, result=[]):
      if n == 0:
        outcomes.append(result)
        return
      for choice in rps:
        find_outcome(n-1, result + [choice])
  find_outcome(n, [])
  return outcomes

  # outcome = []
  # if n == 0:
  #   return []
  # elif n == 1:
  #   return rps
  # else:
  #   for x in rps:
  #     for y in range(0, 3):
  #       outcome.append([x]+[rps[y]])
  #       for z in range(0, len(outcome)):
  #         while len(outcome[z]) < n:
  #           outcome[z].append(rps[y])
  # print(outcome)

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')