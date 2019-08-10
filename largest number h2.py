nor=int(input())
vsr=list(map(int,input().split()))
vsr.sort()
vsr.reverse()
if vsr[0]==0:
    print(0)
else:
    for g in vsr:
        print(g,end='')
