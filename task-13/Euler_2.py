# EULER 2, works
T =  int(input(""))


def FibonacciNumbers(n): 
      
    f1 = 0
    f2 = 1
    next = 1
    sum_boi=0
    
    while next < n: 
        if f2 % 2==0:
            sum_boi += f2
        next = f1 + f2 
        f1 = f2 
        f2 = next        
    return(sum_boi)    

for i in range(T):

    i = int(input(""))
    print(FibonacciNumbers(i))
