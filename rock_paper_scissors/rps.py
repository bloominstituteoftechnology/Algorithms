#!/usr/bin/python

import sys



rps_arr = [[['rock'], ['paper'], ['scissors']]]
new_arr = []
def rock_paper_scissors(n):

  # for i in range(n):
  #   new_arr.append([])
  #   for j in range(n):
  #     new_arr[n].append(rps_arr[0] * n)

  # [['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'], ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'], ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'], ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'], ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'], ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'], ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'], ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']])

  # if n = 0: return []
  # if n = 1: return rps_arr
  # for i in len(n):
  #   new_arr.append(rps_arr[0] * n)
    while n > 0:
      new_arr[n].append(rps_arr[2] * n)
      new_arr[n-1].append(rps_arr[1] * n -1)
      new_arr[n-2].append(rps_arr[0] * n - 2)

  return rock_paper_scissors(n-1)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')