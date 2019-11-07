#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  def construct_list(input_list, remaining_plays):
    if remaining_plays == 0:
      # base case - done: append input_list to output_list
      return output_list.append(input_list)
    else:
      # concatenate rps_list items to input_list and call self n-1 times
      for item in rps_list:
        construct_list([*input_list, item], remaining_plays - 1)

  rps_list = ["rock", "paper", "scissors"]
  output_list = []

  construct_list([], n)
  return output_list
'''
for item in rock_paper_scissors(3):
  print(item)
'''
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
