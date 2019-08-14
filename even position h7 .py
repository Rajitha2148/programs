nor1=int(input())
nor2=input().split()
for zr in range(0,len(nor2)):
    if(zr%2==0):
        if(int(nor2[zr])%2==1):
            print(nor2[zr],end=' ')
    else:
        if(int(nor2[zr])%2==0):
            print(nor2[zr],end=' ')
