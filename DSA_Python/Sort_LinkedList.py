#Sorted Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SortedLinkedList:
    def __init__(self):
        self.head=None
    def insert_sort(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp1=self.head
        #insert node
        Iter=self.head
        while Iter.next:
            Iter=Iter.next
        Iter.next=new_node

        #Sort immediately
        while temp1.next:
            temp2=temp1.next
            while temp2:
                if temp1.data > temp2.data:
                    temp1.data,temp2.data=temp2.data,temp1.data
                temp2=temp2.next
            temp1=temp1.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next

mylist=list(map(int,input("enter list:").split()))
s=SortedLinkedList()
for x in mylist:
    s.insert_sort(x)

s.display()

