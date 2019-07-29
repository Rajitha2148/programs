dr,mn=list(map(int,input().split()))
list1=list(map(int,input().split()))
list2=[]
while(mn):
	kr = list(map(int,input().split()))
	list2.append(kr)
	mn-=1
for ib in list2:
	value=0
	for jb in range(ib[0]-1,ib[1]):
		value=value^list1[jb]
	print(value)
