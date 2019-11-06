#!/usr/bin/python
#outcome=["rock","rock","rock","rock"]if there are four players ... 1 outcome can be this

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  result = []
  players= [0]*n # n is the number of players
  generate_rps(players,0, result)
  return result


def generate_rps(arr,index, result):


    if index == len(arr):
        print(arr)
        result.append(list(arr))
        return arr

    for item in ("rock","paper","scissors"):
        arr[index] =item
        generate_rps(arr,index+1, result)

print(rock_paper_scissors(4))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')