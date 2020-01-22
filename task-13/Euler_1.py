# EULER 1
r = int(input(""))

def multiple_finder(n):
    
    mul_list = []
    
    for i in range(0,n):
        
        if (i%3==0) or (i%5==0):
            
            mul_list.append(i)
    return(sum(mul_list))       


for i in range(r):
    
    inp = int(input(""))
    
    print(multiple_finder(inp))
