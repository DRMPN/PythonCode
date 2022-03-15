# So this function should return the first pair of the two prime numbers spaced
# with a step of g between the limits m, n if these g-steps prime numbers exist
# otherwise None

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def step(g,m,n):
    for i in range(m,n-g):
        if is_prime(i) and is_prime(i+g):
            return[i, i+g]
    return None