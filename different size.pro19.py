sizes8=int(input())
array3=[]
for b in range(sizes8):
	mk=input()
	mk=list(map(int,mk.split(" ")))
	op=len(mk)
	for h in range(op):
		array3.append(mk[h])
array3.sort()
print(*array3,sep=" ")
