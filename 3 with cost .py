d1,r1=map(str,input().split())
m1=0
if len(d1)>len(r1):
  d1,r1=r1,d1
h1=0
while h1<len(d1):
  m1+=(ord(r1[h1])-ord(d1[h1]))
  h1+=1
for q in range(h1,len(r1)):
  m1+=ord(r1[h1])-ord('b')+1
print(m1)
