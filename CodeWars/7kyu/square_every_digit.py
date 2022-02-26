# Welcome. In this kata, you are asked to square every digit of a number 
# and concatenate them. So 9119 -> 811181

def square_digits(num):
    a = ''
    for c in str(num):
        a += str(int(c)**2)
    return int(a)