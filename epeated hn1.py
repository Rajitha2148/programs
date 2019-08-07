try:
	dr=int(input())
	array=list(map(int,input().split()))
	h=[]
	for l in array:
		if array.count(l)>1:
			if l not in h:
				h.append(l)
	print(*h)
	if len(h)==0:
		print("unique")
except ValueError:
	print("invalid")
