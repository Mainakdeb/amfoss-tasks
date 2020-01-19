# bit ++, 282A, works


n = int(input(""))

c = 0

for i in range(n):
    
    inp = input("")
    if "+" in inp:
        c+=1
    elif "-" in inp:
        c-=1
    else:
        pass
    
print(c)    





