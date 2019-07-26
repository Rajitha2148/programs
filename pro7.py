dr=int(input())
ni=0
for hg in range(0,dr):
  if(pow(2,hg)>dr):
    break
  ni=dr-pow(2,hg)
print(ni)
