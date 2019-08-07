ar1=int(input())
br1=pow(2,ar1)
zr1=[]
for k in range(br1):  
    mr1=bin(k).replace("0b","")
    zr1.append(mr1.zfill(ar1))
    zr1.sort(key=(lambda x:x.count('1')))
for k in zr1:
    print(k)
