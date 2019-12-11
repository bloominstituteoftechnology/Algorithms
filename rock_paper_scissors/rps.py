#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps_list = ['rock', 'paper', 'scissors']
  possible = []
  if n == 0:
    return[[]]
  def find_possible(round, round_num):
    for i in range(len(rps_list)):
      round.append(rps_list[i])
      if round_num == n:
        possible.append(round[:])
      else:
        find_possible(round, round_num+1)
      round.pop()

  find_possible([], 1)
  return possible


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')