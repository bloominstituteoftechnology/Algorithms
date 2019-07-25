a = [1,2,3,4,5,2]

seen= set()
dup = set()
for i in a:
  if i not in seen:
    seen.add(i)
  else:
    dup.add(i)

print(dup)
