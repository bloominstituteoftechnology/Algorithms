#!/usr/bin/python

import sys

# --------------------------------------------------------------------------

# RPS 

def rock_paper_scissors(n):
  play = ['rock', 'paper', 'scissors']

  def inner_func(n, huge_list=[]):
      if n == 0:
        return []
      elif n == 1:
        for each in play:
          print(each)
          huge_list.append([each])
        return huge_list
      else:
        # will be populated
        for each in play:
          print(each)
          huge_list.append([each])
        # hopefully

# for each posib, add 3 more posibs to hugelist, take first posib and add a new for each
        print(huge_list, "huge_list")
        count = 0
        bigger_list = []
        for posib in huge_list:
          for again in play:
            print(posib, 'posib from huge list' )
            print(again, "again from play")
            count = count + 1
            bigger_list.append([posib[0], again])
            
            
          # posib.append('rock')

          
          # for again in play:
          #   # print(again)
          #   print(posib,"posib before again")            
          #   posib.append(again)
            # print(posib,"posib after again")
          print(count,"count")
          
            # poss.append(each2)
        return bigger_list
      #   for each in huge_list:
      #     huge_list.append(['paper'])
      #     huge_list.append(['rock'])
      #     huge_list.append(['scissors'])  
      # huge_list.append(['rock'])
      # huge_list.append(['paper'])
      # huge_list.append(['scissors'])
      # else: 
        # return inner_func(n-1, huge_list) + inner_func(n-2, huge_list)

    
      return inner_func(n-1, huge_list) + inner_func(n-2, huge_list)
  
  return inner_func(n)
  pass 



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')