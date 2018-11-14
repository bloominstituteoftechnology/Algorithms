#!/usr/bin/python

import sys
from random import randint

def rock_paper_scissors(n):
  rps = ["rock", "paper", "scissors"]
  randomize = rps[randint(0,2)]
  player = False

  while player == False:
      player = input("\nrock, paper, scissors? ")
      if player == randomize:
        print("\nTie!")

      elif player == "rock":
        if randomize == "paper":
          print("\nYou lose!", randomize, "covers", player)
        else:
          print("\nYou win!", player, "smashes", randomize)

      elif player == "paper":
        if randomize == "scissors":
          print("\nYou lose!", randomize, "cut", player)
        else:
          print("\nYou win!", player, "covers", randomize)

      elif player == "scissors":
        if randomize == "rock":
          print("\nYou lose!", randomize, "smashes", player)
        else:
          print("\nYou Win", player, "cut", randomize)

      else:
        print("\nThat's not a valid play. Check your spelling.")

      player = False
      randomize = rps[randint(0,2)]
      


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')