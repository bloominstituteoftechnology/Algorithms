def nth_fib_iterative(n):
    answer = 0
    n_1 = 1
    n_2 = 0
    for i in range(n-1):
        answer = n_1 + n_2
        n_2 = n_1
        n_1 = answer
    return answer

print(nth_fib_iterative(100))
