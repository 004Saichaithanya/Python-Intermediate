class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        print()
        if self.head is None:
            print("Empty LinkedList")
        temp = self.head
        while temp:
            print(str(temp.data) + "-->", end=" ")
            temp = temp.next

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        iter = self.head
        while iter.next:
            iter = iter.next
        node = Node(data, None)
        iter.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def len_of_LinkedList(self):
        iter = self.head
        count = 0
        while iter:
            count += 1
            iter = iter.next
        return count

    def removeAt(self, index):
        if index < 0 or index >= self.len_of_LinkedList():
            raise Exception("Not Valid Index!")
        if index == 0:
            self.head = self.head.next
            return
        Iter = self.head
        for i in range(index - 1):
            Iter = Iter.next
        Iter.next = Iter.next.next

    def InsertAt(self, index, data):
        len = self.len_of_LinkedList()
        if index < 0 or index > len:
            raise Exception("Not Valid Index!")
        if index == 0:
            self.insertAtBeg(data)
            return
        if index == len:
            self.insertAtEnd(data)
            return
        Iter = self.head
        for i in range(index - 1):
            Iter = Iter.next
        node = Node(data, Iter.next)
        Iter.next = node

    def insert_after_value(self, data_after, data_to_insert):
        Iter = self.head
        while data_after != Iter.data:
            Iter = Iter.next
        node = Node(data_to_insert, Iter.next)
        Iter.next = node

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        Iter = self.head
        while data != Iter.next.data:
            Iter = Iter.next
        Iter.next = Iter.next.next


ll = LinkedList()
# # ll.insertAtBeg(2)
# # ll.insertAtBeg(20)
# # ll.insertAtBeg(5)

# ll.insertAtEnd(30)
# ll.insertAtEnd(5)
mylist = ["banana", "orange", "apple", "mango"]
ll.insert_values(mylist)

ll.insertAtBeg("Melon")
ll.print()

print("\nThe length of Current LinkedList is {}".format(ll.len_of_LinkedList()))

ll.removeAt(0)
ll.print()
print("\nThe length of Current LinkedList is {}".format(ll.len_of_LinkedList()))

ll.InsertAt(3, "Cherry")
ll.print()

ll.insert_after_value("mango", "PineApple")
ll.print()

ll.remove_by_value("banana")
ll.print()
