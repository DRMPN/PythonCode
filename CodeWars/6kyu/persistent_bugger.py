# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you 
# must multiply the digits in num until you reach a single digit.

# (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)

def persistence(n):
    result = 0
    while n > 9:
        tmp = 1
        for i in str(n):
            tmp *= int(i)
        n = tmp
        result += 1
    return result