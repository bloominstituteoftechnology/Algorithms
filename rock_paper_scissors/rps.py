#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  possibleOutcomes = []
  def games(hand, rounds): 
    #[]-hand, 2-round
    #['rock'], 1
    #['rock', 'rock'], 0
    if rounds == 0:
      possibleOutcomes.append(hand)
      return
    for draw in rps:
      games(hand + [draw], rounds - 1)

  games([], n)
  return possibleOutcomes


        


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')