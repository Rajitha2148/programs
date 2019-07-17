d=int(input())

if((d<=10000)and(d>1)):
  for j in range(2,(d//2)+1):
    if((d%j==0)):
      print("no")
      break
      
  else:
    print("yes")
