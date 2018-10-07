#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n==0:
    return [[]]
  elif n==1:
    return [['rock'],['paper'],['scissors']]
  else:
    counter=2
    choices_dict={0:[[]],1:[['rock'],['paper'],['scissors']]}
    while counter<=n:
      last_entry=choices_dict[list(choices_dict.keys())[-1]]
      choices_dict[counter]=[]
      for i in range(len(last_entry)):
        last_entry_item=last_entry[i][0:]
        last_entry_item.append('rock')
        choices_dict[counter].append(last_entry_item)
        last_entry_item=last_entry_item[0:-1]
        last_entry_item.append('paper')
        choices_dict[counter].append(last_entry_item)
        last_entry_item=last_entry_item[0:-1]
        last_entry_item.append('scissors')
        choices_dict[counter].append(last_entry_item)
      counter+=1
  return choices_dict[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')