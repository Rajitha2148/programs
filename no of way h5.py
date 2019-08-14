nor=list(map(str,input()))
set=nor2=0
for f in range(0,len(nor)-1):
  ur=nor[f]
  if int(ur)!=0:
   for g in range(f+1,f+2):
    ur=ur+nor[g]
    if int(ur)<27 and int(ur)>0: set=set+1
    elif int(ur)==0: set=set-1
    else: break
if set!=1: nor2=set%2
print(set+nor2+1)
