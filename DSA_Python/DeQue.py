class DeQUE:
    def __init__(self, MAX):
        self.arr = [''] * MAX
        self.front = -1
        self.rear = -1
        self.MAX = MAX

    def isFull(self):
        return (self.front == 0 and self.rear == self.MAX - 1) or (self.front == self.rear + 1)

    def isEmpty(self):
        return self.front == -1

    def EnqueueRear(self, ele):
        if self.isFull():
            print("Overflow Condition")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.MAX - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = ele  # Assign the element after adjusting rear
        print("Element inserted at rear!")

    def EnqueueFront(self, ele):
        if self.isFull():
            print("Overflow Condition")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.MAX - 1
        else:
            self.front -= 1
        self.arr[self.front] = ele  # Assign the element after adjusting front
        print("Element inserted at front!")

    def DequeueFront(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        temp = self.arr[self.front]
        if self.front == self.rear:  # Queue becomes empty
            self.front = self.rear = -1
        elif self.front == self.MAX - 1:
            self.front = 0
        else:
            self.front += 1
        return temp

    def DequeueRear(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        temp = self.arr[self.rear]
        if self.front == self.rear:  # Queue becomes empty
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.MAX - 1
        else:
            self.rear -= 1
        return temp

    def display(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        i = self.front
        while True:
            print(self.arr[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.MAX
        print()


q = DeQUE(5)

while True:
    print("1.EnqueueFront\t2.EnqueueRear\t3.DequeueFront\t4.DequeueRear\t5.Display\t6.Exit")
    ch = int(input("Enter Choice:"))

    if ch == 1:
        ele = input("Enter element: ")
        q.EnqueueFront(ele)
    elif ch == 2:
        ele = input("Enter element: ")
        q.EnqueueRear(ele)
    elif ch == 3:
        result = q.DequeueFront()
        if result:
            print(f"Element {result} deleted from front!")
    elif ch == 4:
        result = q.DequeueRear()
        if result:
            print(f"Element {result} deleted from rear!")
    elif ch == 5:
        q.display()
    elif ch == 6:
        print("Thank You!")
        break
