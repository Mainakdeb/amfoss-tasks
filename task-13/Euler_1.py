# Euler_1, fails 2 test cases, too slow

t=int(input(""))
for r in range(t):
    
    tot = 0
    
    N=int(input(""))
    
    for i in range(N):
        if i%3==0 or i%5 == 0:
            tot+=i
    print(tot)


