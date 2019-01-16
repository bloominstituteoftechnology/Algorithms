#!/usr/bin/python
import sys

def rock_paper_scissors(n):
  '''
  description:
    generates all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 
  
  pseudo code:
    - hint: inner recursive helper function
    - add an empty list  that will store the mini lists with a '+'
    - have something that represents rock, paper, scissors
    - base case (handles 0), have it return an empty []
    - for loop needed but where?
  '''
  rps = ['rock', 'paper', 'scissors']
  output = []

  def helper(n, result):
    if n == 0:
      output.append(result)
      return

    for play in rps:
      helper(n-1, result+[play])
      
  helper(n, [])
  return output

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')