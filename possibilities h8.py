nor1=int(input())
nor2=input().split()
for d in range(len(nor2)):
    for f in range(d+1,len(nor2)):
        for g in range(f+1,len(nor2)):
            if(int(nor2[d])+int(nor2[f])==int(nor2[g])):
                print(nor2[d],nor2[f],nor2[g])
