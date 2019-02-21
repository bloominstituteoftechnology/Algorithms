# F(n) = F(n-1) + F(n-2)
# F(0) = 0
# F(1) = 1

# add the two before it to get F(n)
# Memoization! by adding cache
cache = {}
def F(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  nth = F(n - 1) + F(n-2)

  cache[n] = nth

  return nth

for i in range(40):
  print(F(i))


def F(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  preprev = 0
  prev = 1
  cur = 0

  for i in range(1, n): 
    cur = prev + preprev

    preprev = prev
    prev = cur

  return cur
