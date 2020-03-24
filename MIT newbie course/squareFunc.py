def square(x):
    '''
    x: int or float.
    '''
    return x**2

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

print(fourthPower(2))

def iterPower(base,exp):
    if exp==1:
        return base
    elif exp>=0:
        return base*iterPower(base,exp-1)
    else:
        return ("broken")