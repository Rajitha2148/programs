nor=input()
flag=0
ip=[int(zr) for zr in input().split()]
for wr in ip:
    if(ip.count(wr)!=1):
        flag=1
        break
if(flag==1):
    print(wr)
else:
    print("unique")
