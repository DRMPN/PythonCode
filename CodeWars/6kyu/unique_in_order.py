# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next 
# to each other and preserving the original order of elements.

def unique_in_order(iterable):
    prev = None
    l = []
    for i in iterable:
        if i != prev:
            l.append(i)
        prev = i
    return l