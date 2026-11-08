#Postfix Eval
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


def div(x,y):
  if y==0:
    raise ZeroDivisionError
  else:
    return x//y

calc={
    "+":lambda x,y:x+y,
    "-":lambda x,y:x-y,
    "*":lambda x,y:x*y,
    "/":lambda x,y:div(x,y)
}
s=Stack()
def postEval(exp):
  
  for x in exp.split():
    if x.isdigit():
      s.push(x)
    else:
      a=int(s.pop())
      b=int(s.pop())
      res=calc[x](b,a)
      s.push(res)
  return s.pop()

exp=input("enter exp:")

print(f"Postfix eval :{postEval(exp)}")




