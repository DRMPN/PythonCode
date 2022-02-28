# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    i = 0
    for n in arr:
        if n > 0:
            i += n
    return i