# So this function should return the first pair of the two prime numbers spaced
# with a step of g between the limits m, n if these g-steps prime numbers exist
# otherwise None

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def step(g, m, n):
    primes = []
    
    for i in range(m, n):
        if is_prime(i):
            print(i)
            primes.append(i)
            
    for i in range(len(primes)):
        num = primes[i]
        for p in primes[i::]:
            if p - num == g:
                return [num, p]
            elif p - num > g:
                break
                
    return None