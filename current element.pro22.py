dt=int(input())
th=list(map(int,input().split()))
tr=[]
po=[]
for i in range(len(th)):
	if i%2==0:
		tr.append(th[i])
	else:
		po.append(th[i])
kl=sum(tr)
gh=sum(po)
if(kl>gh):
	print(kl)
else:
	print(gh)
