
def countsort(a,pos):
    L=len(a)
    count=[0]*10
    res=[0]*L

    for i in range(L):
        temp=(a[i]//pos)%10
        count[temp]+=1
    
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    
    i=L-1
    while i>=0:
        temp=(a[i]//pos)%10
        res[count[temp]-1]=a[i]
        count[temp]-=1
        i-=1
        
    for i in range(L):
        a[i]=res[i]

def radixSort(a):
    M=max(a)
    pos=1
    while M//pos>0:
        countsort(a,pos)
        pos=pos*10



a=[5,1,3,8,4,7,0,2]
radixSort(a)
print(a)