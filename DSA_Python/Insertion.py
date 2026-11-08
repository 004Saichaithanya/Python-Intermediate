a = [4, 5, 2, 8, 9, 1]


# Insertion Sorting
def Insertion(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key




Insertion(a)


print(a)
