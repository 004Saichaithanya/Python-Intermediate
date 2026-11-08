# QUEUE
# list as a Queue
stock_price = []
# use insert() func
stock_price.insert(0, 131.12)  # 0 index:pushing element one by one
stock_price.insert(0, 132.4)
stock_price.insert(0, 135)
stock_price.insert(0, 138.3)
print(stock_price)
print(stock_price.pop())  # FIFO
print(stock_price.pop())
print(stock_price.pop())


#dequeue as QUEUE
from collections import deque
que=deque()
que.appendleft(5)
que.appendleft(10)
que.appendleft(15)
que.appendleft(25)
print(que)
print(que.pop())
print(que.pop())
print(que.pop())


#Queue Class

class Queue:
    def __init__(self):
        self.container=deque()
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isEmpty(self):
        return len(self.container)==0
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.container)
print(q.dequeue())
print(q.dequeue())
print(q.container)
print(q.peek())

print(f"size:{q.size()}")
print(f"Empty:{q.isEmpty()}")
