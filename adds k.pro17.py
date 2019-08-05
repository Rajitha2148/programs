ipl=input()
bjm=list(map(int,ipl.split()))
zdc=bjm[1]
nh=input()
flag21=0
thy=list(map(int,nh.split()))
for l in range(0,len(thy)-1):
	for p in range(l+1,len(thy)):
		if thy[l]+thy[p]==zdc:
			print("yes")
			flag21=1
			break
	if flag21==1:
		break
if flag21!=1:
	print("no")
