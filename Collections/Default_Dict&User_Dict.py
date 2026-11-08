from collections import defaultdict


# default_factory as a lambda
dd = defaultdict(lambda: "Nope")
dd["a"] = 1
dd["b"] = 2
print(dd["a"])
print(dd["b"])
print(dd["c"])  # No KeyError in defaultdict

print(dd.__missing__("a"))
print(dd.__missing__("d"))

# default_factory as a list
d = defaultdict(list)

for i in range(5):
    d[i].append(i)
print(d)

# default_factory as a int
d_int = defaultdict(int)
d_int["a"] = 1
d_int["b"] = 2
print(d_int.items())
print(d_int["c"])


d = {}
d.setdefault("k1", []).append(1)
d.setdefault("k1", []).append(2)
print(d)


from collections import UserDict

print("UserDict:")

dic = {"a": 1, "b": 2, "c": 3}
Ud = UserDict(dic)
print(Ud.data)
print(type(Ud))

Empty_Ud = UserDict()
print(Empty_Ud.data)


# Customizing our own dictionary behaviour we use Userdict


class MyDict(UserDict):
    def pop(self):
        raise RuntimeError("Delection cannot allowd")

    def popitem(self):
        raise RuntimeError("Delection cannot allowd")

    def keys(self):
        raise RuntimeError("Cannot show keys!!")


mydic = MyDict({"a": 1, "b": 2, "c": 3})
print(mydic)

# mydic.popitem()
# print(mydic.keys())
