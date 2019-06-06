def eating_outer(n):
  cache = {}
  def eating_cookies(n, cache=cache):
    
    if n == 3:
      return 4
    elif n == 2:
      return 2
    elif n <= 1:
      return 1

    if n not in cache:
      cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

    return cache[n]
  return eating_cookies(n)  

for i in range(50):
    print(f'{i} : {eating_outer(i)}')
