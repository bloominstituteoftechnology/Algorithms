#!/usr/bin/python

import sys

def rock_paper_scissors(n):
	rps = []
	r = []
	p = []
	s = []
	rock = ["rock"]
	paper = ["paper"]
	scissors = ["scissors"]

	if n == 0:
		print(rps)
	else:

		for i in range(3**n//3):
			r.append(rock)
		for i in range(3**n//3):
			p.append(paper)
		for i in range(3**n//3):
			s.append(scissors)

		for j in range(len(r)):
			print(j)
			if j == 0 or j % 3 == 0:
				r[j] = r[j] + ['rock']
				p[j] = p[j] + ['rock']
				s[j] = s[j] + ['rock']
			if j == 1 or (j - 1) % 3 == 0:
				r[j] = r[j] + ['paper']
				p[j] = p[j] + ['paper']
				s[j] = s[j] + ['paper']
			if j == 2 or (j - 2) % 3 == 0:
				r[j] = r[j] + ['scissors']
				p[j] = p[j] + ['scissors']
				s[j] = s[j] + ['scissors']


		print(r)
		print(p)
		print(s)



print(rock_paper_scissors(1))