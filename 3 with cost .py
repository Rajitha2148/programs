d,r=map(str,input().split())
m=0
if len(d)>len(r):
  d,r=r,d
h=0
while h<len(d):
  m+=(ord(r[h])-ord(d[h]))
  h+=1
for p in range(h,len(r)):
  m+=ord(r[h])-ord('a')+1
print(m)
