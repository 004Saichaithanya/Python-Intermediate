a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def BinarySearch(a, key):
    size = len(a)
    lb = 0
    ub = size - 1
    mid = int((lb + ub) / 2)
    if len(a)==0:
        print("element not found!")
        return
    if a[mid] == key:
        print("Element found")
    elif a[mid] > key:
        BinarySearch(a[lb:mid], key)
    else:
        BinarySearch(a[mid + 1 : ub + 1], key)


BinarySearch(a, 14)
