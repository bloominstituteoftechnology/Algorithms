import itertools
rpsDict = ['rock', 'paper', 'scissors']
listNew = itertools.product(rpsDict, repeat=2)
lis = list(listNew)
empty_list = []
for index, x in enumerate(lis):
    empty_list.append(list(lis[index]))
print(empty_list)
# if n < 0:
#   return []
# elif n == 0:
#   return []
# else:
