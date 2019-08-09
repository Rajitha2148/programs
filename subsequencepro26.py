def subsq(rt): 
    mr = len(rd) 
    subsq = [1]*mr 
    for h in range (1 , mr): 
        for p in range(0 , h): 
            if rd[h] > rd[p] and subsq[h]< subsq[p] + 1 : 
                subsq[h] = subsq[p]+1
    maximum = 0
    for h in range(mr): 
        maximum = max(maximum , subsq[h])  
    return maximum
arr1=int(input()) 
rd = list(map(int,input().split()))
print (subsq(rd))
