kr=int(input())
aray1=list(map(int,input().split()[:kr]))
aray1.sort()
for l in aray1:
  print(l,end=" ")
