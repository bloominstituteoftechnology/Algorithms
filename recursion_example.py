
'''Write a recursive function to count the number of times the integer n appears in the input array
   ex 1. n = 2 [2, 34, 54, 2, 3] should return 2
   ex 2. n = 2 [12, 34, 54, 21, 3]
'''

def count(arr, n):
    if len(arr) < 1:
        return 0

    if arr[0] == n:
        return 1 + count(arr[1:], n)
    else:
        return 0 + count(arr[1:], n)

arr1 = [2, 34, 54, 2, 3]
arr2 = [12, 2, 2, 2]
arr3 = [12, 34, 54, 21, 3]
arr4 = []

print(count(arr1, 2))
print(count(arr2, 2))
print(count(arr3, 2))
print(count(arr4, 2))