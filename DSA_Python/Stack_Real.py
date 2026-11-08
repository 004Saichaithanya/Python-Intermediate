import array

class Stack:
    def __init__(self,type,size):
        self.arr=array.array(type,[0]*size)
        self.top=-1
        self.size=size
    def isFull(self):
        return self.top==self.size-1
    
    def isEmpty(self):
        return self.top==-1
    def push(self,data):
        if(self.isFull()):
            raise Exception("Overflow")
        else:
            self.top+=1
            self.arr[self.top]=data
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow")
        else:
            temp=self.arr[self.top]
            self.top-=1
            return temp
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.arr[self.top]
    
    def printStack(self):
        for i in range(self.top+1):
            print(self.arr[i],end=" ")
        print()
            


s=Stack('i',5)

while True:
    print("1.push,2.pop,3.peek,4.print,5.exit\n")
    ch=int(input("enter ch:"))
    
    if ch==1:
        ele=int(input("Enter ele:"))
        s.push(ele)
    elif ch==2:
        print(s.pop())
    elif ch==3:
        print(s.peek())
    elif ch==4:
        s.printStack()
    elif ch==5:
        print("Thank You!")
        break
    else:
        print("Enter Valid Input!")
            





