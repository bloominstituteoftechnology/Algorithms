#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  signs, results = ['rock', 'paper', 'scissors'], []

  def build_permutation(n_list=[]):
      if len(n_list) < n:
          for sign in signs:
              p_list = n_list[:]
              p_list.append(sign)
              build_permutation(p_list)
      else:
          results.append(n_list)
  build_permutation()
  return results

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
