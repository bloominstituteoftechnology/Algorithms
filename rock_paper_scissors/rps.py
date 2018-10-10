#!/usr/bin/python
import sys
from itertools import product


def rock_paper_scissors(n):
    choices=['rock','paper','scissors']
    outcomes=[]

    def find_result(n, result=[]):
        if n==0:
            outcomes.append(result)
            return

        for choice in choices:
            find_result(n-1, result+[choice])

    find_result(n,[])
    return outcomes







if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
