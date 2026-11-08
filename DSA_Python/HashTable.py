# Hash Table or Hash Map


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):  #updating the key,value if already exists
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:     #if not appending to same hash value index row
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


H = HashTable()
# H.add('march 6',130)
# print(H.get('march 6'))
"""This Operator calls above two functions directly by python
This can be possible by python special functions named __setitem__ &__getitem"""

H["march 6"] = 130
H["march 6"] = 78
H["march 7"] = 200
H["Dec 17"] = 400

H["march 17"] = 459

print(H.get_hash("march 6"))
print(H.get_hash("march 17"))


# print(H.arr)
print(H["march 17"])

del H["march 17"]

# print(H.arr)


H['abc']=18
H['acb']=20

print(H["abc"])

print(H.arr)
