m,r=map(int,input().split())
for num in range(m,r):
    temp=num
    sum=0
    while temp>0:
        digit = temp%10
        sum+=digit**3
        temp//=10
    if (num == sum):
        print(num)
