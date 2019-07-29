
mo,ro = input().split()
mo,ro = int(mt), int(rt)
Lo1 = [ int(x) for x in input().split()]
for i in range(0,ro) :
    ao1,bo1 = input().split()
    ao1,bo1 = int(a01), int(bo1)
for i in range(0,ro):
    print(min(Lo1[ao1-1:bo1]))
