# The parameter of the function find_nb will be an integer m and you have to 
# return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists 
# or -1 if there is no such n.

def find_nb(m):
    i = 0
    while m > 0:
        m -= (i + 1)**3 
        i += 1
    return i if m == 0 else -1