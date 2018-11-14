#!/usr/bin/python

import sys

# Strategy: Start with a list within an output list.  For n iterations, each iteration will take each element within the current output list, append it with 'rock, then make two copies of it and change last element to either 'paper' or 'scissors' to the end, then append these two copies to right after the current element. 

def rock_paper_scissors(n):
  # Initiate an output list
  output = [[]]
  # Iterate n rounds (i.e. n number of elements in each element of output list)
  for i in range(0, n):
    # In each round, iterate through the elements in the current ouput list.  For each element, append the element with'rock', then insert two copies of this element and change the last element to either 'paper' or 'scissors'.
    for j in range(0, len(output)):
      # increase the j value to skip to the next appropriate position due to growing output
      j = j+2*j
      # Append 'rock to current element
      output[j].append('rock')
      # Make copy of the current element, change its last element to 'paper', then insert it 1 position after the current element
      temp_list = output[j].copy()
      del temp_list[len(temp_list) - 1]
      temp_list.append('paper')
      output.insert(j+1,temp_list)
      # Make copy of the current element, change its last element to 'scissors', then insert it 2 positions after the current element
      temp_list = output[j].copy()
      del temp_list[len(temp_list) - 1]
      temp_list.append('scissors')
      output.insert(j+2,temp_list)
      
  # for i in range(0, n):
  #   for j in range(0, len(output)):
  #     temp_list = output[j].copy()
  #     temp_list.append('paper')
  #     output.append(temp_list)     
  #     temp_list = output[j].copy()
  #     temp_list.append('scissors')
  #     output.append(temp_list)
  #     output[j].append('rock')

  return output

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')