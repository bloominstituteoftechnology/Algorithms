#!/usr/bin/python
"""
helper --> function will have a for loop

function --> recursion

list of results

n = rounds of the game

bottom

rock_paper_scissors(n)
rock_paper_scissors(1) ---> playing 1 round ---> all of the possible outcomes

doing a for loop with in a for loop is creating ALL the possible moves in sequential order based on the number of rounds being passed in
"""

import sys

def rock_paper_scissors(roundsRemaining):
  # initialize the initial list
  moves =["rock", "paper", "scissors"] 
  # Initializing an empty array
  outcomes =[]
  # print("Initializing outcomes array:", outcomes)

  #does the recursion --> takes in rounds being passed in. Also passing in the empty array that will be a lists of lists
  def helperfun(roundsRemaining,  result=[]):
    #  base case
      if roundsRemaining == 0: # ---> there are no more plays 
          return outcomes.append(result)
          # print("In if - appending results:", outcomes, "results", results)

      for move in moves:
        # recursive call
        # print("move", move)
        helperfun(roundsRemaining - 1, result + [move])
        # print("recursive call in for:", helperfun)

  helperfun(roundsRemaining)
  
  # print(outcomes)
  return outcomes




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')