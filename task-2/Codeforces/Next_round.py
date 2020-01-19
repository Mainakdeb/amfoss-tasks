# next round 158A, works

l = input("")
l = list(l.split())

n = int(l[0])
k = int(l[1])


p = input("")
p =  list(p.split())


for i in range(n):
    p[i]=int(p[i])
    
p.sort()  

p1 = p[::-1]


g = p1[k-1]


c = 0
for i in range(len(p1)):
    
    p1[i]=int(p1[i])
    if p1[i]>= g: 
        if p1[i]>0:
            c+= 1
        
        
print(c)        
