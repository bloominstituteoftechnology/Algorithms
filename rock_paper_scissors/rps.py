#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays=['rock', 'paper', 'scissors'] 
  end=[]
  def player (n, result):
    if n==0:
      end.append(result)
    else:
      for x in plays:
        player(n-1, result+[x])
  player(n,[])
  return end

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')