from collections import namedtuple

tup = namedtuple("tup", {"x": 0, "y": 0, "z": 0})
t = tup(4, 5, 6)
print(t)

print(t.x, t.y, t.z)
print(t[0])

t = t._replace(x=6)
print(t)

print(t._make(["a", "b", "c"]))
print(t)
print(t.index(5))


Student = namedtuple("Student", ["Name", "Age", "Phone"])
s = Student("Sam", 25, 9999)
print("Student Age is %s" % s[1])

print("Student Phone is {}".format(s[2]))


# Accessing
print(s.Age, s.Name, s.Phone)

name = getattr(s, "Name")

print(f"By using getattr() :{name}")

# _make()
li = ["Suresh", 19, 12345]

s_new = s._make(li)
print(s_new)
d1 = {"Name": "John", "Age": 12, "Dob": "12/05/2012"}
print(s_new._make(d1.values()))

print("Returns as OrderedDict from namedtuple mapped values:")
od = s_new._asdict()

# ** Operator in this way converts Dictionary into namedtuple.But Keys must match .
dic = {"Name": "Ravi", "Age": 20, "Phone": 1111}
print(Student(**dic))

print(s)
print(s._fields)
s = s._replace(Name="Shiva")
print(s)

# li->["Suresh", 19, 12345]
li[0] = "Gopal"
print(Student.__new__(Student, li[0], li[1], li[2]))


# converts namedtuple into normal tuple!
print(s.__getnewargs__())
