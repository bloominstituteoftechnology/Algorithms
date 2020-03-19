
cache = {0: 1, 1: 1}
def recursion_fibonacci(n):
    #base
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1

    # handling cache
    if n in cache:
        return cache[n]
    # if not in cache: 
    cache[n] = recursion_fibonacci(n-1) + recursion_fibonacci(n-2)
    return cache[n]

x=recursion_fibonacci(10)
print(x)

nums = [1,2,3,4,5,6,7,8,9]
def bin_search(arr, val):
    l = 0
    m = len(arr)//2
    r = len(arr) - 1
    while l < r:
        if arr[m] == val:
            return True
        elif val < arr[m]:
            # move left
            return  m -1 
        else:
            # move right 
            return m + 1
    return False

y = bin_search(nums, 5)
print(y)  
