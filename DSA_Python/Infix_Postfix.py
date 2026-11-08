#Infix to Postfix

class Stack:
  def __init__(self):
      self.arr=[]
  def push(self,val):
    self.arr.append(val)
  def pop(self):
    return self.arr.pop()
  def isEmpty(self):
    return len(self.arr)==0
  def peek(self):
    return self.arr[-1]

s=Stack()

op={"+":1,"-":1,"*":2,"/":2,"^":3}
output=[]
def infix_post(exp):
  for x in exp:
    if x.isalnum():
      output.append(x)
    elif x in op:
      while not s.isEmpty() and s.peek() != '(' and op[x]<=op[s.peek()]:
        output.append(s.pop())
      s.push(x)
    elif x == '(':
        s.push(x)
    elif x == ')':
      while not s.isEmpty() and s.peek() != '(':
        output.append(s.pop())
      if not s.isEmpty() and s.peek() == '(':
        s.pop()
  while not s.isEmpty():
    output.append(s.pop())
  return output


exp=input("enter exp:")
output=infix_post(exp)
print("".join(output))



