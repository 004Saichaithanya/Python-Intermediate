a = [1,7,18,5,3,11,9,8,10,2]
# QuickSort


def paritioning(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high

    while True:
        while pivot > a[i] and i < high:
            i += 1
        while a[j] >= pivot and j > low:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

        else:
            break
    a[low],a[j]=a[j],a[low]

    return j


def quicksort(a, low, high):

    if low < high:
        partIndex = paritioning(a, low, high)
        quicksort(a, low, partIndex - 1)
        quicksort(a, partIndex + 1, high)


quicksort(a, 0, len(a) - 1)


print(a)
