class Queue:
    def __init__(self,MAX):
        self.arr=[' ']*MAX
        self.front=-1
        self.rear=-1
        self.MAX=MAX

    def isFull(self):
        return self.rear==self.MAX-1
    
    def isEmpty(self):
        return self.front==-1 or self.front>self.rear
    
    def Enqueue(self,ele):
        if self.isFull():
            raise Exception("Queue Overflow")
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.arr[self.rear]=ele
        print("Inserted!")

    def Dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Underflow!")
        
        temp=self.arr[self.front]
        self.front+=1
        return temp
    
    def display(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        
        for i in range(self.front,self.rear+1):
            print(self.arr[i] ,end=" ")




q=Queue(5)

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

    
