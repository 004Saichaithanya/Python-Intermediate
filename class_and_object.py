class Person:
    amt = 0

    def __init__(self, name, age):
        print("hello person")
        self.name = name
        self.age = age
        Person.amt += 1

    def display(self):
        print(f"name is {self.name} and age is {self.age}")

    def __del__(self):
        Person.amt -= 1
        print("Object deleted!")

    def __str__(self):
        return "Hi Im Object acting like string!"

    @staticmethod
    def get_amt():
        print("amt is", Person.amt)


p1 = Person("sai", 19)
p1.display()
p2 = Person("krishna", 20)

del p1
p2.get_amt()
