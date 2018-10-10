#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    outcomes = []  # outer list, of game sequences [[r,r,r],[r,p,p],[r,p,r],..]

    def find_outcome(n, result=[]):
        # base case
        if n == 0:
            outcomes.append(result)
            return
        # move towards the base case
        for play in plays:
            find_outcome(n - 1, result + [play])  # array flattens automatically

    # Now we need to call the helper function, otherwise it won't run and there is no recusion:
    find_outcome(n, [])
    return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
