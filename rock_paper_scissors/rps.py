#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  pass 

#   n = 3
# moves = ['rock', 'paper', 'scissors']

# def rps(n, moves, x=-1, count=0):
#   game = []
#   count += 1

#   if count > n:
#     return game

#   if x > 2:
#     x = -1
  
#   x += 1
#   game = [[move, moves[x]] for move in moves] 

#   return rps(n, moves)

# print(rps(n, moves))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')