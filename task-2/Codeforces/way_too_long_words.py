# way too long words, works
def shorten(w):
    short = ""
    
    short = w[:1] +str(int(len(w)-2)) + w[-1:]
    
    return(short)


# way too big words
n = input("")
n = int(n)

for i in range(n):
    
    w = input("")
    
    if len(w)>10:
        
        print(shorten(w))
        
    else:
        print(w)
    
    
