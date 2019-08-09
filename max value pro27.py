Aar1,Bbr=map(int,input().split())
Ccr=list(map(int,input().split()))
prr=list(map(int,input().split()))
qrr=[]
arr=0
for i in range(Aar1):
    xr=prr[i]/Ccr[i]
    qrr.append(xr)
while Bbr>=0 and len(qrr)>0:
    minndex=qrr.index(max(qrr))
    if Bbr>=Ccr[minndex]:
        arr=arr+prr[minndex]
        Bbr=Bbr-Ccr[minndex]
    Ccr.pop(minndex)
    prr.pop(minndex)
    qrr.pop(minndex)
print(arr)

