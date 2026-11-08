# list as a Stack DS (not recommended:due to dynamic array expansion and OVERHEAD)
mystack = []
# PUSH
print("LIST:")
mystack.append("youtuble.com/home")
mystack.append("youtube.com/shorts")
mystack.append("youtube.com/profile")
mystack.append("youtube.com/profile/history")
# POP
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
# print(mystack.pop()) Empty stack

# deque as Stack
from collections import deque

print("Dequeue:")
stack = deque()
stack.append("youtuble.com/home")
stack.append("youtuble.com/shorts")
stack.append("youtuble.com/popular")
stack.append("youtuble.com/music")

print(stack.pop())
print(stack)


# Stack Class
print("STACK CLASS:")


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def pushMany(self, list):
        for x in list:
            self.container.append(x)

    def reverse_string(self, text):
        temp = deque()
        temp.extendleft(text)
        rev = ""
        for char in temp:
            rev += char
        return rev

    def reverse(self, text):
        s = Stack()
        for ch in text:
            s.push(ch)
        rev = ""
        while s.size() != 0:
            rev += s.pop()
        return rev


# stk = Stack()
# stk.push("google/search")
# stk.push("google/images")
# stk.push("google/mail")
# print(stk.pop())

# print(stk.peek())
# print(stk.container)
# print(stk.size())
# print(stk.isEmpty())

# stk.pushMany(["mango", "banana", "grapes", "apple"])
# print(stk.container)
# stk.pop()
# print(stk.container)
# stk.pushMany("Hello")
# print(stk.container)

# print(stk.reverse_string("My name is Poloju saichaithanya"))

# print(stk.reverse("Hello"))
