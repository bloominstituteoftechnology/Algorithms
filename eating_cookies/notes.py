n = 3

# def c(n):
#     for i in range(n):
#         sec = n - i 
#         print(sec)
#         for j in range(sec):
#             print(sec - j)

def c(n, count = 0):
    if n < 1:
        return count
    # print(n)
    # print(f'count = {count}')
    # n -= 1
    # for j in l:
    #     l.append(n-j)
    # c(n-1, count+1)
    c(n-1, count+1)
    return c(n-1, count+1)
    # return c(n)

# def c(n, count = 0):
#     if n < 1:
#         return 1
#     print(n)

#     # n -= 1
#     c(n-1, count + 1)
#     print(f'count = {count}')
#     c(n-1, count + 1)
#     print(f'count = {count}')

l = c(n)

print(l)
