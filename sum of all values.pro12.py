mh,rh=list(map(int,input().split()))
lis1=list(map(int,input().split()))
for j in range(rh):
  uh1,vh1=list(map(int,input().split()))
  print(sum(lis1[uh1-1:vh1]))
