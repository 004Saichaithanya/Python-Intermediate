class Person:
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # class methods can access class members directly by cls variable
    def getpopulation(cls):
        return cls.population

    @staticmethod  # static methods can directly pass any variable without self or cls variable
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is ", self.age, " years old")


# both doesnt require instances of class
print(Person.getpopulation())
print(Person.isAdult(20))
newPerson = Person("sai", 19)
newPerson.display()
