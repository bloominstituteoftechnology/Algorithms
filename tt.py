cache=[]
def rock_paper_scissors(n):
  if n <= 1:
    return ['r','p','s']

  
  cache.append(rock_paper_scissors(n-1))
  
  #print(cache)
  return cache

print(rock_paper_scissors(5))
