nor=int(input())
aur=input().split(" ")
aur=[int(nor) for nor in aur]
g=[]
for m in range(0,nor):
  if(m==aur[m]):
    g.append(aur[m])
if not(len(g)==0):
  g=sorted(g)
  for m in range(0,len(g)):
    print(g[m],end=' ')
else:
  print("-1")
