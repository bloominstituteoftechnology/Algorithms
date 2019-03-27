#!/usr/bin/python

import sys

import time

def rock_paper_scissors(n):
  moves = ["rock", "paper", "scissors"]
  answer = []
  newAnswer = []
  if n == 0:
    return answer
  for move in moves:
    answer.append([move])
  for i in range (1,n):
    print('*')
    for move in answer:
      
      m1 = move+[moves[0]]
      newAnswer.append(m1)

      m2 = move+[moves[1]]
      newAnswer.append(m2)

      m3 = move+[moves[2]]
      newAnswer.append(m3)
    answer = newAnswer
    newAnswer = []
  return answer

cmd = input('Enter n: ')
print(rock_paper_scissors(int(cmd)))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')