'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # $#$Start
    '''
    Solution that utilizes bitwise-NOT in order to cancel out numbers we've seen before
    O(n) time and O(1) space
    '''
    answer = 0

    for x in arr:
        answer ^= x

    return answer

    #-----------------------------------------------------------------------------------
    '''
    Solution that utilizes a dict to count occurrences of each number we've seen so far to 
    know which one is the odd-one-out
    O(2n) time and O(n) space
    '''
    # counts = {}

    # # figure out counts of each number in the array
    # for n in arr:
    #     if n in counts:
    #         counts[n] += 1
    #     else:
    #         counts[n] = 1

    # # go through counts dict to find the one number whose value is 1
    # for n, i in counts.items():
    #     if i == 1:
    #         return n    

    # $#$End
    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")