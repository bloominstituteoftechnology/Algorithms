# print that factorial of # n

def rec_factoria(n):
    print(n)
    #base case
    if n <= 1:
        return 1

    #what step can we do recursively?
    prev = rec_factoria(n-1)
    return n * prev

print(rec_factoria(999))
