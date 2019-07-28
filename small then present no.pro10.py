ad=int(input())
rd=list(map(int,input().split()))
md=0
for s in range(0,ad):
  for n in range(0,s):
    if(rd[n]<rd[s]):
      md=md+rd[n]
print(md)
