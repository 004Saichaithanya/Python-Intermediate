class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x / other.x, self.y / other.y) #mul->div

    def __str__(self):
        return "X:{} Y:{}".format(self.x, self.y)  # another way to print on console


v1 = Vector(12, 15)
v2 = Vector(4, 3)
print(v1)
print(v2)
v3 = v1 * v2  # operator overloading :AT Run time Operand * (changes to)-->/
print(v3)
