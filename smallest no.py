r,d=input().strip().split(" ")
d=int(d)
s=0
while s<len(r)-1 and d:
	if(r[s]>r[s+1]):
		d-=1
		r=r[:s]+r[s+1:]
		if(s!=0):
			s-=1
	else:
		s+=1
q=r[:len(r)-d]
print(q)
