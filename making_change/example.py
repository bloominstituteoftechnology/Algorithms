def making_change(amount, denominations, coins_so_far=[]):
    if sum(coins_so_far) == amount:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif denominations == []:
        pass
    else:
        for c in making_change(amount, denominations[:], coins_so_far+[denominations[0]]):
            print(c)
            yield c
        for c in making_change(amount, denominations[1:], coins_so_far):
            print(c)
            yield c


n = 10
denominations = [1, 5, 10, 25, 50]
solution = [s for s in making_change(n, denominations, [])]
print(len(solution))
