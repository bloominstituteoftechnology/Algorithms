'''
A child is running up a staircase that has n steps. The child can hop either 1, 2, or 3 steps at a time. Write a function climbStairs that counts the number of possible ways in which the child can climb the staircase.

For example, for a staircase with n = 3 (the stair has 3 steps), there are 4 ways to climb the staircase:

3 hops of 1
A jump of 1 followed by a jump of 2
A jump of 2 followed by a jump of 1
A single jump of 3
So climbStairs(3) should return 4.
'''

# def naive_climb(n,y):
#     #print(f'before  n {n} {y}')    
#     if n == 0:
#         print(f'return 1 {y}')
#         return 1
#     elif n < 0:
#         #print(f'return 0')
#         return 0
   
#     return(naive_climb(n-2, 2)+naive_climb(n-1,1)) 


# print(naive_climb(3,0))

def countWays(n) : 
    # initialize array to n+1 because res[0] was added.
    res = [0] * (n + 1) 
    '''
    this program is designed specifically for steps 1,2,3.
    Hence defined numbers of ways for taking step 0,1 and 2 .
    '''
    res[0] = 1
    res[1] = 1
    res[2] = 2
      
    '''
    Loop thru steps 0,1 and 2
    range(inclusive, exclusive)
    '''
    for i in range(3, n + 1) : 
        res[i] = res[i - 1] + res[i - 2] + res[i - 3] 
      
    return res[n] 
  
# Driver code 
n = 50
print(countWays(n)) 