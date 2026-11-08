import queue 

q = queue.Queue()

list = [10, 20, 30, 40, 50, 60, 70]

print("Queue :")
for x in list:
    q.put(x)
print(q.get())
print(q.get())

print("Lifo Queue:")
lifo = queue.LifoQueue()
for x in list:
    lifo.put(x)
print(lifo.get())
print(lifo.get())

print("Priority Queue:")
pq = queue.PriorityQueue()
i = 10
for x in list:
    pq.put((i, x))
    i -= 1

while not pq.empty():
    print(pq.get())
