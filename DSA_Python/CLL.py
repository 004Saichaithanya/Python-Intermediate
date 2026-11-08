class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        temp = self.head
        # Traverse to the last node
        while temp.next != self.head:
            temp = temp.next
        # Insert at beginning
        new_node.next = self.head
        self.head = new_node
        temp.next = self.head  # Update last node to point to the new head
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        temp = self.head
        # Traverse to the last node
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head  # Maintain circular reference
    
    def InsertAtPos(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            self.insertAtBeg(data)
            return
        if pos <= 0:
            print("Invalid Position!")
            return
        Iter = self.head
        for i in range(1, pos - 1):
            Iter = Iter.next
            if Iter == self.head:
                print("Position exceeds list size")
                return
        new_node.next = Iter.next
        Iter.next = new_node
    
    def deleteAtBeg(self):
        if self.head is None:
            return
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return
        temp = self.head
        # Traverse to the last node
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head  # Update last node to point to new head
    
    def deleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        Iter = self.head
        # Traverse to the second-last node
        while Iter.next.next != self.head:
            Iter = Iter.next
        Iter.next = self.head  # Remove the last node
    
    def deleteAtPos(self, pos):
        if pos == 1:
            self.deleteAtBeg()
            return
        Iter = self.head
        for i in range(1, pos - 1):
            Iter = Iter.next
            if Iter.next == self.head:
                print("Position exceeds list size")
                return
        Iter.next = Iter.next.next
    
    def display(self):
        if self.head is None:
            print("No list")
            return
        Iter = self.head
        while True:
            print(Iter.data, '-->', end=" ")
            Iter = Iter.next
            if Iter == self.head:
                break
        print(f" (head:{self.head.data})")
    
    def search(self, key):
        if self.head is None:
            print("No list")
            return
        
        Iter = self.head
        while True:
            if Iter.data == key:
                print("Element Found!")
                return
            Iter = Iter.next
            if Iter == self.head:  # Stop when we are back to the head
                break
        
        print("Not found!")
        
        
# Circular Linked List in action
c = CLL()

while True:
    print("1.Insert At Beg\t2.Insert At End\t3.Insert At Pos\t4.Delete At Beg\t5.Delete At End\t6.Delete At Pos\t7.Display\t8.Exit\t9.Search")
    ch = int(input("Enter choice:"))
    if ch == 1:
        ele = input("Enter data:")
        c.insertAtBeg(ele)
    elif ch == 2:
        ele = input("Enter data:")
        c.insertAtEnd(ele)
    elif ch == 3:
        ele = input("Enter data:")
        pos = int(input("Enter position:"))
        c.InsertAtPos(ele, pos)
    elif ch == 4:
        c.deleteAtBeg()
    elif ch == 5:
        c.deleteAtEnd()
    elif ch == 6:
        pos = int(input("Enter position:"))
        c.deleteAtPos(pos)
    elif ch == 7:
        c.display()
    elif ch == 8:
        print("Thank You!")
        break
    elif ch==9:
        key=input("enter key:")
        c.search(key)
