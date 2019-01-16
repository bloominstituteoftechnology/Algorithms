#!/usr/bin/python

import sys
types = ['rock', 'paper', 'scissors']
def rock_paper_scissors(n):

  def game_helper(n, hold, temp):
    if n == 0:
      hold += [temp]
    else:
      for t in types:
         ## Rock ## Rock,Rock  ## Rock ## Rock, Paper
        game_helper(n-1, hold, temp + [t]) ## (2, __, rock) ## (1, __, rock, rock) ## (0, rock,rock, N/A)
                             ## (2, __, rock) ## (1, __, rock, paper) ## (0, rock,rock, N/A)
                                     ## (2, __, rock) ## (1, __, rock, rock) ## (0, rock,rock, N/A)
        ## 1, [], ['rock']
        ## 0, [['rock', 'rock']], ['rock', 'rock'] temp = []
        # 1 [], ['paper']
        # 0 [], ['scissors]
      
    return hold

  game_list = []
  if n == 0:
    game_list.append([])
  else:
    game_list = game_helper(n, [], [])

  print(game_list)
  return game_list



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

