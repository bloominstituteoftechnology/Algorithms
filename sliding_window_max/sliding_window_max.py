'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # $#$Start
    '''
    Naive brute-force approach using two nested loops to calculate the max for each sliding window
    O(n*k) time, O(1) space
    '''
    # init the List that will hold all max values
    # maxs = [0 for _ in range(len(nums) - k + 1)]

    # # loop the sliding window
    # for i in range(len(maxs)):
    #     # grab the element on the left side of the window
    #     curr = nums[i]

    #     # calculate the max value in the sliding window using a linear max algorithm
    #     for j in range(1, k):
    #         if nums[i+j] > curr:
    #             curr = nums[i+j]

    #     maxs[i] = curr

    # return maxs

    #----------------------------------------------------------------------------------------------
    '''
    Solution that utilizes a Queue
    We'll maintain the invariant that the front element of the Queue will be the max value of the window at all times

    O(n) time, O(k) space
    '''
    from collections import deque

    maxs = []
    q = deque()

    for i, n in enumerate(nums):
        # remove elements from the Queue so long as the current number is greater that the element
        while len(q) > 0 and n > q[-1]:
            q.pop()
        
        # add the number once all smaller numbers have been evicted from the Queue
        q.append(n)

        # calculate the window range 
        window = i - k + 1

        # so long as the window's range == k, we'll add elements to the Queue
        if window >= 0:
            # add the max element, in this case the first element in the Queue, to the output List 
            maxs.append(q[0])

            # check if the number on the left side of the window is going to be evicted in the next iteration
            # if it is, and if that value is at the front of the Queue, we need to evict it from the Queue
            if nums[window] == q[0]:
                q.popleft()

    return maxs

    # $#$End
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
