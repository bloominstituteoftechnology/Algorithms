# Sliding Window Max

Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

## Example
```
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 ```

 Can you implement a solution that calculates all of the maximum sliding window values in O(n) time?

 ## Testing 
Run the test file by executing  `python test_sliding_window_max.py`. 

There is also a larger test file that you can test your code against by running `python test_sliding_window_max_large_input.py`.

> Note: The text files in the `data/` directory are used by the large input tests. 