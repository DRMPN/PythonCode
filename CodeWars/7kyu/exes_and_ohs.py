# Check to see if a string has the same amount of 'x's and 'o's. The method 
# must return a boolean and be case insensitive. The string can contain any 
# char.

def xo(s):
    xsos = 0
    for c in s.lower():
        if c == 'x':
            xsos += 1
        elif c == 'o':
            xsos -= 1
    return xsos == 0
