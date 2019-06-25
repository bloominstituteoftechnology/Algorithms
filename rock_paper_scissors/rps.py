#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [["rock"],["paper"],["scissors"]]
    else:
        result = []
        print('hi',result)
        prev = rock_paper_scissors(n - 1)
        print('hey', prev)
        for combo in prev:
            for choice in ["rock", "paper", "scissors"]:
                newCombo = combo.copy()
     
                newCombo.append(choice)
 
                result.append(newCombo)
           
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')