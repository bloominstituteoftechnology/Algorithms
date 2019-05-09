from time import time

# READ IN WORDS FROM FILE
f=open('words.txt', 'r')
words=f.read().split("\n")
f.close()

def second_pass_anagrams(words):

	# Create a dictionary that will hold the key/value pairs
	# of character & count of times character exists in the word

	anagrams = {}

	longest = None

	for word in words:
		# get a signature, lowercase, sorted word
		signature = "".join(sorted(word.lower()))
		# check if signature is in anagrams, if it's not then add it
		if signature not in anagrams:
			anagrams[signature] = []
		# then add word itself to the signature/key in dictionary
		anagrams[signature].append(word)

		# Update the largest set as we create them
		if longest == None or len(anagrams[signature]) > len(anagrams[longest]):
			longest = signature

	print(anagrams[longest])

    
def third_pass_anagrams(words):
    # create new dictionary
    anagrams = {}

    # GENERATE ALL SETS OF ANAGRAMS
    for word in words:
        # convert list to string
        signature = "".join(sorted(word.lower()))
        if signature not in anagrams:
            anagrams[signature] = []
        anagrams[signature].append(word)

    # FIND LARGEST SET OF ANAGRAMS
    maxLen = 0
    maxAnagrams = []
    for signature in anagrams:
        if len(anagrams[signature]) > maxLen:
            maxLen = len(anagrams[signature])
            maxAnagrams = anagrams[signature]

    print(maxAnagrams)


# Algorithm to time our code

# Store a startin time
start_time = time()

# Run our code
second_pass_anagrams(words)

# Store the ending time
end_time = time()
second_pass_total_time = end_time - start_time

# Store a startin time
start_time = time()

# Run our code
third_pass_anagrams(words)

# Store the ending time
end_time = time()
third_pass_total_time = end_time - start_time

print (f"Anagrams 2nd pass time {second_pass_total_time}")
print (f"Anagrams 3rd pass time {third_pass_total_time}")