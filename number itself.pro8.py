import math
cr22,l23=map(int,input().split())
mr25=[]
kr12=list(map(int,input().split()))
for i in range(0,l23):
    pr12,qr32=map(int,input().split())
    mr25.append([pr12,qr32])
for i in mr25:
    xr23=i[0]-1
    yr24=i[1]-1
    print(math.gcd(kr12[xr23],kr12[yr24]))
