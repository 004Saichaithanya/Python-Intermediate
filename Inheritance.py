class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(self.name, " ", self.age, " ", self.salary)


W1 = Worker("sai", 20, 200000)
W1.display()
