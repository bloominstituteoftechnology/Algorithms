#!/usr/bin/python

import sys

def rock_paper_scissors(n, plays = None):
  if plays == None:
    plays = []
    for i in range(3 ** n):
      plays.append([])
    return rock_paper_scissors(n, plays)
  elif len(plays) < 3:
    return plays
  else:
    rock = plays[:int(len(plays)/3)]
    paper = plays[int(len(plays)/3):int(2 * len(plays)/3)]
    scissors = plays[int(2 * len(plays)/3):]
    for play in rock:
      play.append('rock')
    for play in paper:
      play.append('paper')
    for play in scissors:
      play.append('scissors')

  return rock_paper_scissors(n // 3, rock) + rock_paper_scissors(n // 3, paper) + rock_paper_scissors(n // 3, scissors)
  
  # return rock_paper_scissors(n // 3, plays[:len(plays)/3]) + rock_paper_scissors(n // 3, plays[len(plays)/3:2 * len(plays)/3]) + rock_paper_scissors(n // 3, plays[2 * len(plays)/3:])





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print('')
    print(rock_paper_scissors(num_plays))
    print('')
  else:
    print('Usage: rps.py [num_plays]')