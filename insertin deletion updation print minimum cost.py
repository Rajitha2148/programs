dr,pop=input().split()
cost_diffe=abs(len(dr)-len(pop))
for j in range(len(dr)):
    if len(pop)==1 and pop[j] in dr:
        break
    if dr[j] != pop[j]:
        cost_diffe+=1 
print(cost_diffe)
