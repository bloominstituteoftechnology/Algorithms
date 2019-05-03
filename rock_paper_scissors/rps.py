#!/usr/bin/python

import sys


# def rec_rps(players, fixed, count, main_list=[], sub_list=[], string="", i=0):
#   list_val = ['rock', "scissor", 'paper']
#   if count == 0:
#     return main_list
#   else:
#     if players == 0:
#       count -= 1
#       return rec_rps(fixed, fixed, count, main_list, sub_list, list_val[i], i)
#     elif players > 0:
#       if string == "":
#         string = list_val[i]
#       sub_list.append(string)
#       if i == 2:
#         i = 0
#       else:
#         i += 1
#       return rec_rps(players-1, fixed, count, main_list, sub_list, list_val[i], i)
#     return main_list.append(sub_list)
  

# def rock_paper_scissors(n):
#   return rec_rps(n, n, 9)


    
  

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', "scissor", 'paper']

  def rec_rps(n, result=[]):
    # print(f"result: {result}")
    if n == 0:
      return outcomes.append(result)
    for play in plays:
      rec_rps(n-1, result + [play])
    
  rec_rps(n, [])
  return outcomes

# print(rock_paper_scissors(2))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
