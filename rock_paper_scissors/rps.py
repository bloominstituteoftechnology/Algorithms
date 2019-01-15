#!/usr/bin/python
import random
import sys

def rock_paper_scissors(n):
  plays = []
  playChoices = ['rock','paper', 'scissors']
  
  def recursionMemes(n, templist = []):
    if n < 1:
      plays.append(templist)
      return 'end'
    for play in playChoices:
      n = n-1
      recursionMemes(n, templist + [play] )

  recursionMemes(n, [])
  return [play for play in plays if len(play) == n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')