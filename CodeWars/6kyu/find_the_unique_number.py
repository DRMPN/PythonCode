# There is an array with some numbers. All numbers are equal except for one. 
# Try to find it!

def find_uniq(arr):
    s = iter(set(arr))
    for n in s:
        if arr.count(n) > 1:
            return next(s)
        else:
            return n