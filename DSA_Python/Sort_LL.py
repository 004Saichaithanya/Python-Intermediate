class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        Iter=self.head
        while Iter.next:
            Iter=Iter.next
        Iter.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print()
    
    def sort(self):
        temp1=self.head
        temp2=self.head.next
        while temp1.next:
            temp2=temp1.next
            while temp2:
                if temp1.data>temp2.data:
                    temp1.data,temp2.data=temp2.data,temp1.data
                temp2=temp2.next
            temp1=temp1.next
s=SLL()
while True:
    print("Insert\t2.display\t3.sort\t4.exit")
    ch=int(input("enter choice:"))
    if ch==1:
        ele=input('enter data:')
        s.insertAtEnd(ele)
    elif ch==2:
        s.display()
    elif ch==3:
        s.sort()
    elif ch==4:
        break