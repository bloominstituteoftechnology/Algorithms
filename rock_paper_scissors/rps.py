#!/usr/bin/python
"""
output =[]
first pass
output=[[rock], [paper], [scissors]]
second pass
output=[[rock, rock], [rock,paper], [rock,scissors], [paper, rock], [paper, paper], [
    paper,scissors], [scissors,rock], [scissors,paper], [scissors,scissors]]

base case accounts for the number of plays
in recursive calls to append to the inner lists

"""
import sys


def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  plays = []
  def rock_paper_scissors_helper(options,n):
    if n == 0:
      plays.append(options)
    else:
      for item in rps:
        rock_paper_scissors_helper(options + [item], n - 1 )
  rock_paper_scissors_helper([],n)
  return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
