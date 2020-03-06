#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #Define list of plays and possibilites
  plays = ["rock", "paper", "scissors"]
  all_poss = []
  
  #Helper function to keep track of the amt or rounds left and the results
  def rounds(rleft,res):
    

    if rleft== 0:
      all_poss.append(res)
      return
    
    for i in range(0,len(plays)):
      rounds(rleft -1, res + [plays[i]])
    
  rounds(n,[])
  return all_poss
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')