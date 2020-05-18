'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #$#$Start
    '''
    Solution that uses two pointers that start on either end of the array, counting 0s as the pointers move 
    If the left pointer sees a 0 and the right pointer sees a non-zero, we swap their values
    Otherwise, we increment the left pointer if it sees a non-zero value
    We decrement the right pointer if it sees a 0
    O(n) time, O(1) space
    '''
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1
    
    return arr

    #$#$End
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")