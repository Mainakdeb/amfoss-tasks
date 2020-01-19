# diagonal difference, works
n = input("")
n = int(n)
big_list=[]

for i in range(n):
    l = input("")
    l = list(l.split())
    
    for x in range(n):
        l[x]= int(l[x])
    big_list.append(l)    
        
def diagonalDifference(arr):
    
    d1 = 0
    d2 = 0
    c1 = 0
    c2=-1
    
    for i in range(len(arr)):
        d1 = d1 + arr[i][c1]
        d2 = d2 + arr[i][c2]
        c1 += 1
        c2 -=1
        
    print(abs(d1-d2))
diagonalDifference(big_list)    
