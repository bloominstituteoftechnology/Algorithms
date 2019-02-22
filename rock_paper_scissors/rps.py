#!/usr/bin/python

import sys

def rock_paper_sci(n):
	rps = []
	empty_list = [["rock"],["paper"],["scissors"]]
	r = []
	p = []
	s = []
	rock = ["rock"]
	paper = ["paper"]
	scissors = ["scissors"]


	if n == 0:
		print(rps)

	if n == 1:
		return [rock, paper, scissors]
	else:

		# for i in range(3**n//3):
		# 	r.append(rock)
		# for i in range(3**n//3):
		# 	p.append(paper)
		# for i in range(3**n//3):
		# 	s.append(scissors)
		# print(r)
		# print(p)
		# print(s)

		# print(rps)
		
		

		def rps_rounds(n, rps_list):
			new_list = []
			r = []
			p = []
			s = []
			if n == 1:
				print(rps_list)
				return rps_list
			else:
				for i in rps_list:
					new_list.append(i + rock)
					new_list.append(i + paper)
					new_list.append(i + scissors)
				# print(new_list)
				rps_rounds(n-1, new_list)


			# rps_rounds(n-1,rps_list)
		

			
		print(rps_rounds(n,empty_list))

print(rock_paper_sci(2))