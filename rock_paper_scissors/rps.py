#!/usr/bin/python

import sys
import random
from collections import deque
def rock_paper_scissors(n):
  stack=[[]]
  list_of_ways= [['rock'],['paper'],['scissors']]

 

  
  if n==0:
     return stack

  if n==1:
     
     return list_of_ways
      
  if n>1:
    y=0
    stack.remove(stack[0])
    while y<n:
     for i in range(n):
       player_one = random.choice(list_of_ways)
       player_two = random.choice(list_of_ways)
       result= [player_one[0],player_two[0]]
       stack.append(result)
       y+=1
  return stack


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')