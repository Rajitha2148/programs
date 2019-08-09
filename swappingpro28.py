arrd=int(input())
brrd=[int(sd) for sd in input().split()]
brrd.sort()
sd=0
xvd=0
for o in range(len(brrd)):
    if brrd[o]>=sd:
        xvd+=1
    sd=sd+brrd[o]
print(xvd)
