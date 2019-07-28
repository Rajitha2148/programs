mr=int(input())
cr=0
lr=[]
for j in range(1,mr+1):
  lr.append(j)
for j in range(len(lr)):
  for j in range(j+1,len(lr)):
    cr+=1
print(cr)
