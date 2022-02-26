# Complete the findNextSquare method that finds the next integral perfect 
# square after the one passed as a parameter. Recall that an integral perfect 
# square is an integer n such that sqrt(n) is also an integer.


from math import sqrt


def find_next_square(sq):
    root = sqrt(sq)
    if root % 1 == 0:
        root += 1
        return root * root
    else:
        return -1