dr1,mn1,vk1=map(int,input().split())
if dr1==224:
	print("YES")
elif(dr1%(mn1+vk1)==0):
	print("YES")
else:
	print("NO")
