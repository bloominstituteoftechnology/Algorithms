
rpsDict = {0: "rock", 1: "paper", 2: "scissors"}
print(rpsDict[0])
empty_list = []
inner_list = []

for i in range(2):

    for j in range(2):
        print(j)
        inner_list.append(rpsDict[i])
        inner_list.append(rpsDict[j])


print(inner_list)
# if n < 0:
#   return []
# elif n == 0:
#   return []
# else:
