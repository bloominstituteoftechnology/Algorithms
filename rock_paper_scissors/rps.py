#!/usr/bin/python
import random
import sys

def rock_paper_scissors(n):

  playChoices = ['rock','paper', 'scissors']
  plays = [[]]
  while count < 5:
    for i in range(n):
      x = random.randint(0,2)

  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')