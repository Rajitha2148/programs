checkkr1=int(input())
validdr1=list(map(int,input().split()[:checkkr1]))
validdr1.sort()
queer1=int((len(validdr1))/2)
print(validdr1[queer1])
