class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
    def insertAtBeg(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        self.head.prev=newNode
        newNode.next=self.head
        self.head=newNode
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        Iter=self.head
        while Iter.next:
            Iter=Iter.next
        Iter.next=newNode
        newNode.prev=Iter
    def insertAtPos(self,data,pos):
        newNode=Node(data)
        if pos==1:
            self.insertAtBeg(data)
            return
        if pos<0:
            print("Invalid")
            return
        Iter=self.head
        for _ in range(1,pos-1):
            Iter=Iter.next
        newNode.next=Iter.next
        Iter.next.prev=newNode
        Iter.next=newNode
        newNode.prev=Iter

    def deleteAtBeg(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    
    def deleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        Iter=self.head
        while Iter.next.next:
            Iter=Iter.next
        Iter.next=None
    
    def deleteAtPos(self,pos):
        if pos==1:
            self.deleteAtBeg()
            return
        if pos<=0:
            print("Invalid")
            return
        Iter=self.head
        for i in range(1,pos-1):
            Iter=Iter.next
        Iter.next=Iter.next.next
        Iter.next.prev=Iter

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print()

    def search(self,key):
        if self.head is None:
            print('No list')
            return
        Iter=self.head
        while True:
            if Iter.data==key:
                print('element found')
            if Iter.next==None:
                break
            Iter=Iter.next
        print('element Not found')
    
    def insertMany(self,List:list):
        class Node:
            def __init__(self,data):
                self.data=data
                self.next=None
        
        class SLL:
            def __init__(self):
                self.root=None
            def insertatend(self,data):
                newNode=Node(data)
                if self.root is None:
                    self.root=newNode
                    return
                Iter=self.root
                while Iter.next:
                    Iter=Iter.next
                Iter.next=newNode
        sll=SLL()
        for x in List:
            sll.insertatend(x)
        return sll.root
                

    
    def two_Lists(self):
        List1=[]
        List2=[]

        temp1=self.head
        while temp1:
            List1.append(temp1.data)
            temp1=temp1.next
        print(List1)

        tail=self.head
        while tail.next:
            tail=tail.next
        while tail:
            List2.append(tail.data)
            tail=tail.prev
        print(List2)
        root1=None
        root2=None
        root1=self.insertMany(List1)

        print("\nForward List:")
        while root1:
            print(root1.data,end="-->")
            root1=root1.next


        root2=self.insertMany(List2)
        print("\nBackward List:")
        while root2:
            print(root2.data,end="-->")
            root2=root2.next


        



        
        


d=DLL()
while True:
    print("\n1.InsertAtBeg\t2.InsertAtEnd\t3.InsertAtPos\t4.DeleteAtBeg\t5.DeleteAtEnd\t6.DeleteAtPos\t7.Display\t8.Search\t9.Split Two Lists\t10.Exit")
    ch=int(input("enter choice:"))
    if ch==1:
        ele=input("enter data:")
        d.insertAtBeg(ele)
    elif ch==2:
        ele=input("enter data:") 
        d.insertAtEnd(ele)
    elif ch==3:
        ele=input("enter data:")
        pos=int(input("enter pos:"))
        d.insertAtPos(ele,pos)
    elif ch==4:
        d.deleteAtBeg()
    elif ch==5:
        d.deleteAtEnd()
    elif ch==6:
        pos=int(input("enter pos:"))
        d.deleteAtPos(pos)
    elif ch==7:
        d.display()
    elif ch==8:
        key=input('enter key:')
        d.search(key)  
    elif ch==9:
        d.two_Lists()
    elif ch==10:
        break   

