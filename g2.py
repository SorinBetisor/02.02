with open("cifre2.txt","r") as f:
    n=f.readline()
a=True
k=-2
for e in n:
    k+=1
    if n[k]<n[k+1]:
        a=True
    else:
        a=False
        break

if a:
    print('Da')
else:
    print('Nu')