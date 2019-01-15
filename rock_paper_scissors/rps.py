#!/usr/bin/python

import sys
#  Your output should be a list of lists containing strings.
#  Each inner list should have length equal to the input n.


def rock_paper_scissors(n):
    array = []
    options = ['rock', 'paper', 'scissors']
    if n == 0:
        return [array]
    if n == 1:
        for o in options:
            array.append([o])
        return array
    for i in range(0, 3 ** n):
        array.append([options[0]]*n)
    return array


print(rock_paper_scissors(1))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')