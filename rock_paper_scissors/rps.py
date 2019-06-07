#!/usr/bin/python
'''
3^n outputs.
Each output contains n combination.
n loop of [r,p,s]
let n = 2 => [r,p,s] => [r,r] [r,p][r,s]....
             [r,p,s]

'''
import sys

"""
Recursive implementation that exhibits O(3^n) runtime
"""
def rock_paper_scissors_recursive(n):
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

"""
Iterative implementation or rps
"""
def rock_paper_scissors_iterative(n):
  output = []
  possible_plays = ['scissors', 'paper', 'rock']

  stack = []
  stack.append([])

  while len(stack) > 0:
    hand = stack.pop()

    if n == 0 or len(hand) == n:
      output.append(hand)
    else:
      for play in possible_plays:
        stack.append(hand + [play])

  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
