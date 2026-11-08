class CirQue:
    def __init__(self,MAX):
        self.arr=[' ']*MAX
        self.front=-1
        self.rear=-1
        self.MAX=MAX

    def isFull(self):
        return (self.rear + 1) % self.MAX == self.front
    
    def isEmpty(self):
        return self.front==-1
    
    def Enqueue(self,ele):
        if self.isFull():
            print("Queue Overflow!")
            return
        if self.isEmpty():
            self.front=0
        self.rear=(self.rear+1)%self.MAX
        self.arr[self.rear]=ele
        print("Inserted!")

    def Dequeue(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        temp=self.arr[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.MAX
        return temp
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        i=self.front
        while True:
            print(self.arr[i],end=" ")
            if i==self.rear:
                break
            i=(i+1)%self.MAX
        print()





q=CirQue(5)

while True:
    print("1.Enqueue\t2.Dequeue\t3.display\t4.Exit")
    ch=int(input("Enter Choice:"))

    if ch==1:
        ele=input("Enter element:")
        q.Enqueue(ele)
    elif ch==2:
        print("Element {} deleted!".format(q.Dequeue()))
    elif ch==3:
        q.display()
    elif ch==4:
        print("Thank You!")
        break

    
