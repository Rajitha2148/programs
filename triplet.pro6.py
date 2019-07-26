dr=int(input())
set=list(map(int,input().split()))
gon=0
for c1 in range(dr):
    for u2 in range(c1,dr):  
        for h3 in range(u2,dr):
            if set[c1]<set[u2]<set[h3]:
                gon+=1
print(gon)
