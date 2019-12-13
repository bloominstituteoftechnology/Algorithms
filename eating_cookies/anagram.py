

"""

def is_anagram(s0, s1):

	s0 = normalize(s0)

	s1 = normalize(s1)

​

	return s0 == s1

"""

​

def normalize(s):

	return ''.join(sorted(list(s.lower())))  # alphabetical version

​

def find_anagrams(words):

	anagrams = {}

​

	for w in words:

		signature = normalize(w)

​

		if signature not in anagrams:

			anagrams[signature] = []

​

		anagrams[signature].append(w)   # ["dog", "god"]

​

	longest = []

​

	for a in anagrams:

		if len(anagrams[a]) > len(longest):

			longest = anagrams[a]

​

	print(longest)

​

words = []

​

with open('words.txt') as fp:

	for line in fp:

		words.append(line.strip())

​

find_anagrams(words)

