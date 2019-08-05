lon,kgf=map(int,input().split())
ls1t=[]
for b in range(lon):
    ls1t.append(input())
for xd in range(len(ls1t)):
    if('0' in ls1t[xd]):
        ls1t[xd]=ls1t[xd].replace('0','')
    ls1t[xd]=ls1t[xd].replace(' ','')
lengthss=[]
for xd in ls1t:
    if(len(xd)>0):
        lengthss.append(len(xd))
kgf=min(lengthss)
rt1='1 '*kgf
rt1=rt1.strip()
for xd in range(kgf):
    print(rt1)
