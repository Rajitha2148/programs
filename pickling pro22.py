numr=int(input())
ar=list(map(int,input().split()))
pr=[]
qr=[]
for i in range(len(ar)):
	if i%2==0:
		pr.append(ar[i])
	else:
		qr.append(ar[i])
sr=sum(pr)
rd=sum(qr)
if(sr>rd):
	print(sr)
else:
	print(rd)
