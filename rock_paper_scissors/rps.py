#!/usr/bin/python

import sys

def rock_paper_scissors(n):
 
  # output = [[]]
  
  # for i in range(0, n):
  #   for j in range(0, len(output)):
      
  #     j = j+2*j
      
  #     output[j].append('rock')
      
  #     temp_list = output[j].copy()
  #     del temp_list[len(temp_list) - 1]
  #     temp_list.append('paper')
  #     output.insert(j+1,temp_list)
  #     temp_list = output[j].copy()
  #     del temp_list[len(temp_list) - 1]
  #     temp_list.append('scissors')
      # output.insert(j+2,temp_list)
      
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



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')