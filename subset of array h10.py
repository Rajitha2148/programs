nor1,nor2= map(int,input().split())
arrr1 = list(map(int,input().split()))
arrr2 = list(map(int,input().split()))
fr =1
for i in arrr2:
    if i not in arrr1:
        print('NO')
        fr = 0
        break
if(fr):
    print('YES')
