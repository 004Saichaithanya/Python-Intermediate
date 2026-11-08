class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtBeg(self,data):
        node=Node(data)
        temp=self.head
        self.head=node
        node.next=temp
    
    def InsertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)
    
    def InsertAtPos(self,data,pos):
        if self.head is None:
            self.head=Node(data)
            return
        i=0
        temp=self.head
        while(i<pos-1):
            temp=temp.next
            i+=1
        node=Node(data)
        node.next=temp.next
        temp.next=node
    
    def rotate(self,k):
        if not self.head or k==0:
            return
        temp=self.head
        length=1
        while temp.next:
            temp=temp.next
            length+=1
        temp.next=self.head
        k=k%length
        #print(length)

        new_tail=self.head
        step_count=length-k-1
        for _ in range(step_count):
            new_tail=new_tail.next
        self.head=new_tail.next
        new_tail.next=None


    def insertMany(self,lis):
        for x in lis:
            self.InsertAtEnd(x)

    def print(self):
        print()
        if self.head is None:
            print("Empty LinkedList")
        temp = self.head
        while temp:
            print(str(temp.data) + "-->", end=" ")
            temp = temp.next

Ll=LinkedList()
# Ll.InsertAtBeg(10)
# Ll.InsertAtBeg(20)
# Ll.InsertAtBeg(30)

# Ll.print()
# Ll.InsertAtEnd(50)
# Ll.print()

# Ll.InsertAtPos(1000,2)
# Ll.print()

# Ll.InsertAtEnd(1)
# Ll.InsertAtEnd(5)
# Ll.InsertAtEnd(3)
# Ll.InsertAtEnd(4)
# Ll.InsertAtEnd(2)
# Ll.print()

# Ll.rotate(3)
# Ll.print()
# Ll.insertMany([10,1,2,9,8,2])
# Ll.print()
# Ll.rotate(5)
# Ll.print()

Ll.insertMany([1,5,3,4,2])
Ll.print()
Ll.rotate(3)
Ll.print()




        