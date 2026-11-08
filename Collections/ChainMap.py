from collections import ChainMap

d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "d": 4}
d3 = {"f": 5}

c = ChainMap(d3, d2, d1)  # takes only first duplicate key value pair in ChainMap
print(c)

# Operations on ChainMap

print(list(c.keys()))
print(list(c.values()))
print(c.maps)

c1 = ChainMap(d1, d2)
print(c1.maps)

c2 = c1.new_child(d3)
print(c2.maps)

print(c2["a"])
# a value gets reversed with latest value
c2.maps = reversed(c2.maps)
print(c2["a"])
print(c2)
