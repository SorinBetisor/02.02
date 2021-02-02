with open("cifre.txt","r") as f:
    n=f.readline()
e=[]
impare=0
pare=0
for digit in n:
    e+=digit
for d1 in e:
    if (int(d1)%2==0) or (int(d1)==0):
        pare+=1
    elif (int(d1)%2!=0):
        impare+=1
print(
'In numar sunt ',pare,' cifre pare'
)
print(
    'In numar sunt ',impare,' cifre impare'
)


