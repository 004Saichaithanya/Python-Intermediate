# func=lambda x:x+5
# print(func(10))

# multiple arguments in lambda
# func=lambda x,y:x+y
# print(func(5,5))

# lambda in another functions
# def add7(z):
#     func=lambda x:x+10
#     return func(10)+z
# print(add7(5))

# lambda on map and filter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList1 = list(map(lambda x: x + 5, a))
print(newList1)
newList2 = list(filter(lambda x: x % 2 != 0, a))
print(newList2)
