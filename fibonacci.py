#F(n) = F(n-1) + F(n-2)

"""def F(n):
    if n < 2:
        return n 

    return F(n-1) + F(n-2)
    
for i in range(10):
    print(F(i))"""

#this isnt optimized because computing previous two numbers in sequence to get the next so slows for larger n
#so exponential O(2^n)
#memoization can cache numbers and then look up later so dont have recalculate

#top down approach
#create dictionary for cache
cache = {}

def F_memo(n):
    if n < 2:
        return n 
#look up to see if number is already in cache
    if n in cache: 
        return cache[n]
#calculate nth fib number
    nth == F(n-1) + F(n-2)

    #if in cache use it
    cache[n] == nth

    return nth
    
for i in range(10):
    print(F_memo(i))


#bottom up approach
def F(n):
    if n < 2:
        return n 

    prevprev == 0
    prev == 1
    current == 0
    
    for i in range(1, n):
        current == prev + prevprev

        prevprev == prev
        prev == current

    return current

"""for i in range(10):
    print(F(i))"""

print(F(1000))