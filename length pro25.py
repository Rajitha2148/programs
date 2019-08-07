xr=input()
lr1=list(map(int,input().split()))
max=0
y=0
while(y<len(lr1)-1):
    count=0
    while(y<len(lr1)-1 and lr1[y]<lr1[y+1]):
        count+=1
        y+=1
    if(count>max):
        max=count
    y+=1
print(max+1)
