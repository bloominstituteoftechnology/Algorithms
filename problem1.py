# def binary_search(arr, target):
#     # Set boundaries for low and high marks to search
#     lo = 0
#     hi = len(arr)
#     # While low and high do not overlap...
#     while lo < hi:
#         # Check the midpoint
#         mid = (lo + hi) // 2
#         # If it's equal, return True
#         if arr[mid] == target:
#             return True
#         # Else, if target is smaller
#         elif target < arr[mid]:
#             # set the high to midpoint value
#             hi = mid
#         # Else if target is bigger
#         else:
#             # set the low to midpoint value
#             lo = mid + 1
#     # If we get to the end, return False
#     return False

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 