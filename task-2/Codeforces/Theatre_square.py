# theatre square, works
l = input("")
l = list(l.split())
for i in range(3):
    l[i]= int(l[i])
    
n = l[0]
m = l[1]
a = l[2]


if m%a == 0 :
    k1 = int(m/a)
else:
    
    k1 = int(m/a) + 1
    
if n%a == 0 :
    k2 = int(n/a)
else:
    
    k2 = int(n/a) + 1    
    
    
print(k1 * k2)
