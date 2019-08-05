opi=int(input())
l21=list(map(int,input().split()))
yt=[1]*opi
for vc in range(opi):
    if(vc==0):
        if(l21[vc]>l21[vc+1]):
            yt[vc]=yt[vc]+yt[vc+1]
    elif(vc>0):
        if(l21[vc]>l21[vc-1]):
            yt[vc]=yt[vc]+yt[vc-1]
print(sum(yt))
