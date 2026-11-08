a=[6,2,4,1,7,5]

Minindex=0

for i in range(len(a)-1):
    Minindex=i
    for j in range(i+1,len(a)-1):
        if a[j]<a[Minindex]:
            Minindex=j
    a[i],a[Minindex]=a[Minindex],a[i]


print(a)
