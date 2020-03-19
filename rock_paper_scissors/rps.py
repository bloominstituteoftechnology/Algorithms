#!/usr/bin/python

import sys

def add_one_more(list_plays):
    list_return = []
    strings = [['rock'],['paper'],['scissors']]
    for i in list_plays:
        for j in strings:
            list_return.append(i+j)
    return list_return
    

def rock_paper_scissors(n):
    if n <= 0:
        return [[]]
    else:
        return add_one_more(rock_paper_scissors(n-1))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')