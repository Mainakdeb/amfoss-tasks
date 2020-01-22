
def is_pal(n):

    num=str(n)
    if len(num)==5:
      if num[0] == num[-1] and num[1]==num[-2] :
          return True
    elif len(num)==6:
      if num[0] == num[-1] and num[1]==num[-2] and num[2]==num[-3]:
        return True
    elif len(num)==7:
      if num[0] == num[-1] and num[1]==num[-2] and num[2]==num[-3] and num[3]==num[-4]:
        return True    



def sort(newList):
  newList.sort()
  return newList    

t=int(input(""))

for g in range(t):

  listb=[]
  n=int(input(""))


  for i in range(100,1000):
      for j in range(100,1000):
          #print("f2")
          pd = i*j

          if is_pal(pd):
            if pd>n:
              break
            else:  
              listb.append(pd)
              

  #listb=sort(listb)
  #bprint((listb))
  print(max(listb))
