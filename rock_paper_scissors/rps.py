#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  # set list of plays 
  plays =['rock', 'paper', 'scissors',]
  #set empty list of all possible plays to be appended
  all_poss =[]
  
  def roundkeeper( roundsleft, result):
    # bases case: if roundsleft == 0 return the append empty array to all_pos array
    if roundsleft == 0:
      all_poss.append(result)
      return

   
   #loop through each play 
    for i in range( 0, len(plays)):
     # call function decrementing round down and adding plays to result array
      roundkeeper(roundsleft -1, result + [plays[i]])

  roundkeeper(n, [])
  return all_poss
  
rock_paper_scissors(0)
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')