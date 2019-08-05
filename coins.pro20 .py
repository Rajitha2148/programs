nt,mt=list(map(int,input().split()))
lst=list(map(int,input().split()))
lst.sort(reverse=True)
kl=0
for j in lst:
    if mt==0:
        break
    yu=mt // j
    kl+=yu
    mt=mt-j*yu
print(kl)
