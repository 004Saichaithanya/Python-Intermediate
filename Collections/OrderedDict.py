from collections import OrderedDict

# Note:In Python(3.7+) Regular dict can maintain Insertion Order when changes!
print("Regular Dict:")
d = {"a": 1, "b": 2, "c": 3, "d": 4}
for key, value in d.items():
    print(key, value)

print("After Update:")
d["c"] = 5

for key, value in d.items():
    print(key, value)

# Key value Change
print("Ordered Dict:")
od = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])
for key, value in od.items():
    print(key, value)

od["c"] = 5
print("After Update:")
for key, value in od.items():
    print(key, value)

# Equality Comparison

od1 = OrderedDict({"s": 0, "a": 1, "b": 2, "c": 3, "d": 45})
od2 = OrderedDict({"c": 3, "b": 2, "a": 1})
print(od1 == od2)
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 3, "b": 2, "a": 1}
print(d1 == d2)

# Ordered Dict Reversal

rev_dict = OrderedDict(reversed(list(od1.items())))
print(rev_dict)

# popitem last item
print(od1.popitem(last=True))
print(od1.pop("b"))
print(od1)


od1.move_to_end("s")
print(od1)

od1.move_to_end("c", last=False)  # goes to start
print(od1)


print(od2)

od2.pop('c')
print(od2)
od2['c']=3
print(od2)
