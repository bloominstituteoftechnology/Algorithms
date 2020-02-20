n = 3

# def c(n):
#     for i in range(n):
#         sec = n - i 
#         print(sec)
#         for j in range(sec):
#             print(sec - j)

def c(n, count = 1):
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

# def eating_cookies(n, cache=1):
#     if n < 1:
#         return cache
#     eating_cookies(n-1, cache+1)
#     return eating_cookies(n-1, cache+1)


# l = eating_cookies(n)

# l = c(n)

# print(l)


# for i in n:
#     n = n-i
#     i -= 1
n = 3
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0 :
        return 1
    else:
        a = eating_cookies(n-1)
        print(f'a = {a}')
        b = eating_cookies(n-2)
        print(f'b = {b}')
        c = eating_cookies(n-3)
        print(f'c = {c}')
        total = a + b + c
        print(f'a + b + c = {a + b + c}')
        return total

print(eating_cookies(n))