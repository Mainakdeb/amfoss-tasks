# EULER 3, works
def prime_factors(n):
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


t = int(input(""))

for i in range(t):
    
    p = int(input(""))
    pfs = prime_factors(p)
    largest_prime_factor = max(pfs)
    print(int(largest_prime_factor))
