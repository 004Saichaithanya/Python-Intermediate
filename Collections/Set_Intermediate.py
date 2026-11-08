set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
print(set1)

set1.add(9)
print(set1)


set1.update([1, 11, 12, 13, 14, 0, -1])  # argument can be any iterative
print(set1)

set1.remove(2)  # if element not exits raises ERROR
print(set1)

set1.discard(11)  # if element not exits  does not raises ERROR
print(set1)

set1.pop()  # deletes random element from set
print(set1)

print("Set Operations:")
s1 = {0, 1, 3, 5, 7, 9, 11}
s2 = {0, 2, 4, 6, 8, 10, 11}
print(s1 | s2)  # union() or update()
print(s1 & s2)  # intersection()
print(s1 - s2)  # difference()
print(s1 ^ s2)  # symmetric_difference()


# Set Comprehension
thislist = [2, 5, 10, 3, 15, 50, 35, 23]
set2 = {str(x) for x in thislist if x % 5 == 0}
print(set2)
