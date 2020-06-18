'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our
        # recursive logic to calculate it, and then save the answer in our
        # cache for future uses
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache)
    return cache[n]

