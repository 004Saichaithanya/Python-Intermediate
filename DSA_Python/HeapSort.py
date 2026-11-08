class HeapSort:
    def __init__(self):
        self.arr=[]
        self.sorted_arr=[]
    def insert(self,data):
        self.arr.append(data)
        self.heapify_up(len(self.arr)-1)
    def heapify_up(self,index):
        if index==0:
            return
        parent=(index-1)//2
        if self.arr[index]<self.arr[parent]:
            self.arr[index],self.arr[parent]=self.arr[parent],self.arr[index]
            self.heapify_up(parent)

    def deleteMin(self):
        if len(self.arr)==0:
            return
        if len(self.arr)==1:
            return self.sorted_arr.append(self.arr.pop())
        root=self.arr[0]
        self.sorted_arr.append(root)
        self.arr[0]=self.arr.pop()
        self.heapify_down(0)
    def heapify_down(self,index):
        left=2*index+1
        right=2*index+2
        small=index 
        if left<len(self.arr) and self.arr[small]>self.arr[left]:
            small=left
        if right<len(self.arr) and self.arr[small]>self.arr[right]:
            small=right

        if index!=small:
            self.arr[small],self.arr[index]=self.arr[index],self.arr[small]  
            self.heapify_down(small)

minHeap = HeapSort()
myarr = [3, 1, 7, 8, 21, 89, 100, 10]
for x in myarr:
    minHeap.insert(x)

print("Min Heap after inserting:")
print(minHeap.arr)

# Deleting min elements to create a sorted array
while len(minHeap.arr) != 0:
    minHeap.deleteMin()

print("Sorted array:")
print(minHeap.sorted_arr)
