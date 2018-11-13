#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n:

    moves = [['rock'], ['paper'], ['scissors']]
    lista = moves.copy()
    while n > 1:
      for move in moves:
          move_r = move.copy()
          move_p = move.copy()
          move_s = move.copy()
          move_r.append('rock')
          move_p.append('paper')
          move_s.append('scissors')
          lista.append(move_r)
          lista.append(move_p)
          lista.append(move_s)
          lista.remove(move)
      moves = lista.copy()
      n -= 1
    return  lista
  else:
      return [[]]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')