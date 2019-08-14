nor1=int(input(""))
arrr=list(map(int,input().split()))
length=len(arrr)
larr=max(arrr)
sr,ur=0,0
for g in range(0,length-1):
 for s in range(g+1,length):
  if abs(arrr[g]+arrr[s])< larr:
   sr,ur=arrr[g],arrr[s]
   larr=abs(sr+ur)
print(sr, ur)
