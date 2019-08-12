try:
	nor=int(input())
	numr1=list(map(int,input().split()))
	for g in numr1:
		if numr1.count(g)==1:
			print(g)
except ValueError:
	print("invalid")
