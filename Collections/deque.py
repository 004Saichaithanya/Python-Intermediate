from collections import deque

dq = deque([1, 2, 3, 4, 5])
print(dq)
dq.append("a")
print(dq)
dq.appendleft("z")
print(dq)

dq.extend([8, 9, 10])
print(dq)
dq.extendleft("hello")
print(dq)

dq.rotate(-1)
print(dq)
print(dq.pop())
print(dq.popleft())

dq.remove("e")
print(dq)
dq.reverse()
print(dq)
# dq.clear()
# print(dq)

print("More Operations:")
print(dq)
print(dq.index(4, 0, 6))  # ele,start,end(exclusive)

dq.insert(3, "w")  # index,value
print(dq)
dq.remove("z")
print(dq)
dq.extend([1, 2, 3, 2])
print(dq)
print(dq.count(2))  # (value)No.of occurance of value in dq

print("Current size of dq {}".format(len(dq)))
