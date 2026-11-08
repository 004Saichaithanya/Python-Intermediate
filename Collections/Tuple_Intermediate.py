# Note:Tuples are Unchangable & Immutable!
thistuple = "apple"  # ("apple",)
print(type(thistuple))  # without comma it returns string as type!

tup = tuple(["apple", "banana", "grapes", "mango"])
print(tup)

# Adding tuple to a tuple
t1 = (1, 2, 3, 4, 5)
t2 = ("a", "e", "i", "o", "u")
t1 += t2
print(t1)

# Unpacking the Tuple
fruits = ("apple", "mango", "cherry", "chilli")
(green, yellow, *red) = fruits  # NO.of variables must match the elements in the tuple.
# else use arstirk on remaining
print("green " + green)
print("yellow " + yellow)
print(f"red {red[0]} and {red[1]}")
