# List Comprehension :
fruits = ["apple", "banana", "grape", "melon", "anger", "add"]
fruits[0]="green apple"
print(fruits)
newlist = []

newlist = [x.upper() for x in fruits if x.startswith("a")]
print(newlist)


# Customized Sorting In List :
thislist = [(1, 2), (3, 1), (4, 2)]
thislist.sort(key=lambda x: x[1])
print(thislist)

data = [
    {"name": "alice", "age": 18},
    {"name": "kiran", "age": 15},
    {"name": "Bhanu", "age": 22},
]
data.sort(key=lambda x: x["age"])  # sort by age
print(data)


def custom_sort(s):
    return len(s)


fruits.sort(key=custom_sort)
print(fruits)
