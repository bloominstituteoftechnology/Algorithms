#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
# 	options = ['rock','paper','scissors']
# 	def rps(game_plays,n):
# 		if n == 0:
# 			return [[]]
# 		else:
# 			game_plays = rps(game_plays,n-1)
# 			games = []
# 			for o in options:
# 				for g in game_plays:
# 					games.append(g + [o] )
# 			return games
# 	return rps([],n)


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [["rock"],["paper"],["scissors"]]
    else:
        result = []
        prev = rock_paper_scissors(n - 1)
        for combo in prev:
            for choice in ["rock", "paper", "scissors"]:
                newCombo = combo.copy()
                newCombo.append(choice)
                result.append(newCombo)
        return result




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')