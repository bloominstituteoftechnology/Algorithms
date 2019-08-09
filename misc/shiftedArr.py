def shifted_arr_search(shiftArr, num):
    pivotIdx = findPivot(shiftArr)
 
    # pivot = 0 when whole array is in ascending order
    # or [5,4,0,1,2,3], num=1
    if (pivotIdx == 0) or num < shiftArr[0]:
        return binarySearch(shiftArr, pivotIdx, len(shiftArr)-1, num)
    else:
        return binarySearch(shiftArr, 0, pivotIdx-1, num)

def binarySearch(a, left, right, num):
    while left <= right:
        mid = (right+left) // 2

        if a[mid] == num:
            return mid
        elif a[mid] < num : # [0,1,2,3,4,5] num =5
            left = mid + 1
        elif a[mid] > num : # [0,1,2,3,4,5] num =0
            right = mid - 1

    return -1


  
def findPivot(a):
    left = 0
    # if not -1 from len(a), the "=" in 'left <= right' will fail 
    # calculating mid=(right) + left)//2 . eg a=[1,2]
    right = len(a) - 1  

    while left <= right :
        mid = (right + left) // 2
        #mid=0 when left=right=0 [5,0,1,2,3,4]
        #print(f'l {left} r {right} m {mid} a {a[mid]}')
        if a[mid] < a[mid -1] or mid == 0:  
            return mid

        if a[mid] > a[0] :    # [0,1,2,3,4,5] 
            left = mid + 1      # mid already known to be not the pivot
     
        if a[mid] < a[0]:     # [5,0,1,2,3,4]  
            right = mid-1

    return 0

#a=[1,2,3,4,5,0] # pivot=5
a = [5,0,1,2,3,4]   # pivot=1
a = [1,2]
n=1
print(shifted_arr_search(a,n))