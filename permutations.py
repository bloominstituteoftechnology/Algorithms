def helper(words, remain):
    if not remain:
        return words
    else:
        new_words = []
        for i in range(len(remain)):
            new_words.extend(helper(
                [w + remain[i] for w in words], [letter for j, letter in enumerate(remain) if j != i]))
        return new_words


def permutations(word):
    return helper([''], list(word))


print(permutations('hello'))
