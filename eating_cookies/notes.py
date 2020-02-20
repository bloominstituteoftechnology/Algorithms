
# n = 3

# def c(n):
#     for i in range(n):
#         sec = n - i 
#         print(sec)
#         for j in range(sec):
#             print(sec - j)

# def c(n, count = 1):
#     if n < 1:
#         return count
#     # print(n)
#     # print(f'count = {count}')
#     # n -= 1
#     # for j in l:
#     #     l.append(n-j)
#     # c(n-1, count+1)
#     c(n-1, count+1)
#     return c(n-1, count+1)
#     # return c(n)

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
# n = 3
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0 :
#         return 1
#     else:
#         a = eating_cookies(n-1)
#         print(f'a = {a}')
#         b = eating_cookies(n-2)
#         print(f'b = {b}')
#         c = eating_cookies(n-3)
#         print(f'c = {c}')
#         total = a + b + c
#         print(f'a + b + c = {a + b + c}')
#         return total

# print(eating_cookies(n))


# n = 3

# l = [1] * 3

# print(l)

# print(sum(l))

# def ty(n):
#     l = [1] * n
#     print(l)
#     if l[0] == 1:
#         l[1] = n - l[0]
#         l[2] = n - (l[0] + l[1])
#         print(l)
#     if l[0] == 2:
#         l[1] = n - l[0]
#         l[2] = n - (l[0] + l[1])
# ty(n)


# def ty(n):
#     l = [1] * n
#     for i in range(len(l)):
#         if l[i] == 1:
#             l[n-]


#get fibinocci by index
#for reference [0,1,1,2,3,5,8,13,21]
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(5))
#to use a cache, you need to put things in and get things out
cache = {}
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    else:[p]
        value = fib(n-1) + fib(n-2)
        cache[n] = value
        return value

print(fib(6))
#The lookup time of a value of an array is O^1