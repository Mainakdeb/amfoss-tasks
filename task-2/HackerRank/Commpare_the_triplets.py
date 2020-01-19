# compare the triplets, works
a = input("")
b = input("")



a = list(a.split())
b = list(b.split())

for i in range(3):
    a[i],b[i]=int(a[i]), int(b[i])
def compareTriplets(a,b):
    a_points=0
    b_points=0

    for i in range(3):
        if a[i]>b[i]:
            a_points+=1
        elif a[i]<b[i]:
            b_points+=1
        else:
            pass
    arr = [a_points,b_points]  
    
    return(arr)
    
    
print(*compareTriplets(a,b), sep=" ")    
   
