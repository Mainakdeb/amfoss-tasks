# time conversion, works
t = input("")
h = int(t[0:2])
ap = t[-2]

def timeConversion(t):
    
    h = int(t[0:2])
    
    if ap == "P":
        
        if h == 12:
            
            return(t[0:-2])
        
        time = str(12+h)+t[2:-2]

        return(time)


    if ap == "A":

        if h == 12:

            return("00"+t[2:-2])
        else:


            time =t[0:-2]

            return(time)    
        
print(timeConversion(t))        
