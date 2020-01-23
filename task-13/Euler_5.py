# Euler_5, works
def check(n, upperLimit):
    for i in range(1, upperLimit+1):
        if n%i==0:
            continue
        else:
            return False
    return True


T = int(input(""))
for r in range(T):

  upperLimit=int(input(""))
  if upperLimit>=10 and upperLimit<=20:
    x = 2520
  elif upperLimit>20:
    x = 232792560
  elif upperLimit<10:
    x = 1



  while not check(x, upperLimit):
      if upperLimit>10 and upperLimit<=20:
          x= x+2520
          
      if upperLimit>20:
          #print("flag")
          x= x+232792560

      if upperLimit<10:
        x = x+1    
      
  print(x)    
    

# 2520 for 1-10
# 232792560 for 1-20
