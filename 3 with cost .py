dr,n=map(str,input().split())
y=0
if len(dr)>len(n):
  dr,n=n,dr
bj=0
while bj<len(dr):
  y+=(ord(n[bj])-ord(dr[bj]))
  bj+=1
for bj in range(bj,len(n)):
  y+=ord(n[bj])-ord('a')+1
print(y)
