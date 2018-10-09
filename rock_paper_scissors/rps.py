#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  pass 

# game = []
#   count += 1

#   if count > n * 3:
#     return game
#     print('returns')

#   if x > 1:
#     x = -1
  
#   x += 1
#   game.extend([[move, moves[x]] for move in moves]) 
#   print(game)
#   return rps(n, moves, x, count)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')