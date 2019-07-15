
import os
number1=int(input())
lst=[]
for i in range(number1):
    lst.append(input())
print(os.path.commonprefix(lst))
