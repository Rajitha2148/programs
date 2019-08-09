xaar1 = int(input())
taar = int(xaar1/2)
raar = []
for h in range(xaar1, taar, -1):
    o = str(h)
    if h + sum([int(kaar) for kaar in o]) == xaar1:
        print(1)
        print(h)
        break
else:
    print(0) 
