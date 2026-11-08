from collections import Counter

a = Counter("banana")
print(a)
b = Counter(["a", "a", "b", "c"])
print(b)
c = Counter({"a": 1, "b": 2, "c": 0})
print(c)
d = Counter(dogs=4, cats=7)
print(d)
print(Counter(A=3,B=5,C=2))

# Methods
print(c.most_common(2))
print(list(d.elements()))
print(c.clear())

# operations
print("Operaions:")
c = Counter(a=1, b=2, c=0, d=-1)
li = ["a", "b", "d", "a"]
c.subtract(li)
c.update(li)  #similar to union    
print(c)

a1 = Counter(["a", "a", "b", "c", "c", "c", "d"])
a2 = Counter(a=2, b=3, c=1, d=1)
print(a1 + a2)
print(a1 - a2)
print(a1 & a2)  # intersection
print(a1 | a2)  # union


mylist=[1,1,2,2,2,3,4]
print(Counter(mylist))
print('Counter Methods:')

count=Counter('abracadara')
print(count)
print(count.keys())
print(count.values())
print(count.items())
print(count.get('a'))
