m=int(input(" "))
r=m
d=0
while(r>0):
   d=d+(r%10)**3
   r=r//10
if(d==m):
  print('yes')
else:
  print('no')
