#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  def recursion_helper(list):
	  possibilities = [['rock'],['paper'],['scissors']]
	  new_list = []
	  for item in list:
	    for possibility in possibilities:
	      new_list.append(item + possibility)
	  return new_list

  if n == 0:
    return [[]]
  count = 1
  answer = [['rock'], ['paper'], ['scissors']]
  if n == 1:
    return answer
  while count < n:
    answer = recursion_helper(answer)
    count += 1
  return answer
	
	

print(rock_paper_scissors(2))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')