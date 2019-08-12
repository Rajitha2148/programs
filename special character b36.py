dr=input()
rr=0
for k in range(len(dr)):
  if(dr[k].isdigit() or dr[k].isalpha() or dr[k]==(" ")):
    continue
  else:
    rr+=1
print(rr)
