def iterPower(base,exp):
    result=1
    while exp>0:
        result*=base
        exp-=1
    return result
print(iterPower(2,3))

def gcdIter(a, b):
    i = a if a<b else b
    while a % i or b % i:
        i -= 1
    return i
print(gcdIter(2,6))

