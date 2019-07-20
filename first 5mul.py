number33=int(input())
if(number33==0):
  for product in range(0,5):
    print(0,end=" ")
else:
  for product in range(1,6):
    print(product*number33,end=" ")
