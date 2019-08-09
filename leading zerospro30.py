anyad1=(input())
catad=0
for i in range(0,len(anyad1)):
    surad=(anyad1[:i]+anyad1[i+1:])
    if(int(surad) % 8==0):
        catad=1
        break
if(catad==1):
    print("yes")
else:
    print("no")
