#!/usr/bin/python

import sys

validPlays = [["rock"], ["paper"], ["scissors"]]

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  if n == 1:
    return validPlays

  output = []

  arrA = rock_paper_scissors(n - 1)

  for subArr in arrA:
    for play in validPlays:
      newPlay = subArr + play
      output.append(newPlay)

  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')