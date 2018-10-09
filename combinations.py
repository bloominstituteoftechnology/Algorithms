# research and practice
# number of arrangements 

def nck_recursive(n,k):
  if k ==0 or k ==n:
    return 1
  else:
    return nck_recursive(n-1,k) + nck_recursive(n-1,k-1)

print(nck_recursive(2,1))


def fact(n):
  if n <= 1:
    return 1
  else:
    return n*fact(n-1)
    
print(fact(1))

def nck_factorial(n,k):
  return fact(n)/(fact(k) * fact(n-k))


def nck_multiplicative(n,k):
  result = 1
  for i in range(1,k-1):
    result = result * (n-(k-i))/i
  return result
