#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # $#$Start
  """
  Recursive implementation that exhibits O(3^n) runtime
  """
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result=[]):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for play in plays:
      find_outcome(rounds_left - 1, result + [play])

  find_outcome(n, [])
  return outcomes


# def rock_paper_scissors_iterative(n):
#   """
#   Iterative implementation or rps
#   """
#   output = []
#   possible_plays = ['scissors', 'paper', 'rock']

#   stack = []
#   stack.append([])

#   while len(stack) > 0:
#     hand = stack.pop()

#     if n == 0 or len(hand) == n:
#       output.append(hand)
#     else:
#       for play in possible_plays:
#         stack.append(hand + [play])

#   return output

  # $#$End
  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')