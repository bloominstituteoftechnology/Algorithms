#!/usr/bin/python
import sys
#n = number of plays per round + list length 
#output = all of the possible plays



def rock_paper_scissors(n,combos = []):

  list = ['rock', 'paper', 'scissors']  
  if combos is None:
        combos = []

  if len(list) == n:

    if combos.count(list) == 0:
      combos.append(list)
      combos.sort()
    return combos
  
  else:

    for i in range(len(list)):
      refined_list = list[:i] + list[i+1:]
      combos = rock_paper_scissors(n, refined_list, combos)

    return combos



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')