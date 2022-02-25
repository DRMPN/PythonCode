# Given an array of integers your solution should find the smallest integer.

# ASSUME: arr is not empty
def find_smallest_int(arr):
    i = None
    for n in range(len(arr)):
        if i is None:
            i = arr[n]
        elif i > arr[n]:
            i = arr[n]
    return i
    # return min(arr)