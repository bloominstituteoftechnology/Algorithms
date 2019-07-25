def anagrams1(words):
    anagrams = {}

    for word in words:
        alphaform = "".join(sorted(word.lower()))
        #print(f'{word} {alphaform}')

        if alphaform not in anagrams:
            anagrams[alphaform] = []

        anagrams[alphaform].append(word)

    for key in anagrams:
        print(anagrams[key])

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

anagrams1(words)
