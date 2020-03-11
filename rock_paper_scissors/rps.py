#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  # generate a list of POSSIBLE plays given (n) number of plays per a round of Rock Paper Scissors
  
  # Strategy
    # recursively call a recursively call helper function (n) times, reducing (n) on each call

    # keep track of the options played (array) in the round using memoization, 
    # by passing in the options played into the recursive play() function
    
    # keep appending to the options played memoization each recursive call

    # when (n) reaches 0, base case is reached, and the results are returned.
  
  results = []
  options = ['rock', 'paper', 'scissors']

  def play(options_played, plays_left):
    
    # base case - once we've gone through all the plays
    if plays_left == 0:
      results.append(options_played)
    
    else:
      # for each number of plays in a round (n)
      # call play and append to options played
      for i in range(0, n + 1):
        for j in range(0, len(options)):
          options_played.append(options[j])
        play(options_played, plays_left - 1)

  play([], n) # kicks off recursion 
  return results

print(rock_paper_scissors(1))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')