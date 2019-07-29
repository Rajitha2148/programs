
mf,rf = input().split()
mf,rf = int(mf), int(rf)
Lf1 = [ int(x) for x in input().split()]
for i in range(0,rf) :
    af1,bf1 = input().split()
    af1,bf1 = int(af1), int(bf1)
for i in range(0,rf):
    print(min(Lf1[af1-1:bf1]))
