#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n==0:
    return [[]]
  else:
    counter=1
    choices_dict={0:[[]]}
    while counter<=n:
      last_entry=choices_dict[list(choices_dict.keys())[-1]]
      choices_dict[counter]=[]
      for i in range(len(last_entry)):
        last_entry_item=last_entry[i]
        choices_dict[counter].append(last_entry_item+['rock'])
        choices_dict[counter].append(last_entry_item+['paper'])
        choices_dict[counter].append(last_entry_item+['scissors'])
      counter+=1
  return choices_dict[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')