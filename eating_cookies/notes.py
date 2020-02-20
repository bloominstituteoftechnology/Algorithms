n = 3

# l = [1] * 3

# print(l)

# print(sum(l))

def ty(n):
    l = [1] * n
    print(l)
    if l[0] == 1:
        l[1] = n - l[0]
        l[2] = n - (l[0] + l[1])
        print(l)
    if l[0] == 2:
        l[1] = n - l[0]
        l[2] = n - (l[0] + l[1])
ty(n)


def ty(n):
    l = [1] * n
    for i in range(len(l)):
        if l[i] == 1:
            l[n-]