vr=int(input())
mj=list(map(int,input().split(" ")))
mj=[bin(p) for p in mj]
mj.sort(reverse=True)
mj=[int(vr,2) for vr in mj]
for p in range(0,vr):
     print(mj[p])
