#!/usr/bin/python
#  * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
#  * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.
# * You'll want to define a list with all of the possible Rock Paper Scissors plays.


import sys

def rock_paper_scissors(n):
  # define possible plays, and make list of  possibleoutcomes 
  outcomes = [] 
  plays = ['rock', 'paper', 'scissors']

  # make helper function that can take the rounds left (n), and the result(empty [])
  #  as long as there are plays left, for every item in the plays array, it will add it to the results array  
  # if there are no rounds left, it will take all the results and put it in the outcomes array
  #  call the helper function, and return the outcomes array to get your answer
  def possibleOutcomes(roundsLeft, result):
    if roundsLeft == 0:
      outcomes.append(result)
      return
    for play in plays:
      possibleOutcomes(roundsLeft - 1, result + [play])

  possibleOutcomes(n,[])
  return outcomes



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')